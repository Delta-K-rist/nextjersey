from django.shortcuts import render, redirect, get_object_or_404
from main.forms import ProductForm
from main.models import Product

from django.http import HttpResponse
from django.core import serializers

from django.contrib import messages
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required

import datetime
from django.http import HttpResponseRedirect, JsonResponse
from django.urls import reverse
from django.views.decorators.csrf import csrf_exempt
from django.views.decorators.http import require_POST
from django.utils.html import strip_tags

import requests

@login_required(login_url='/login')
def show_main(request):
    filter_type = request.GET.get("filter", "all")  # default 'all'

    if filter_type == "all":
        product_list = Product.objects.all()
    else:
        product_list = Product.objects.filter(user=request.user)

    context = {
        'npm' : '2406425810',
        'name': 'Deltakristiano Kurniaputra',
        'class': 'PBP C',
        'product_list': product_list,
        'last_login': request.COOKIES.get('last_login', 'Never'),
        'username': request.user.username
    }

    return render(request, "main.html", context)

def create_product(request):
    form = ProductForm(request.POST or None)

    if form.is_valid() and request.method == "POST":    
        product = form.save(commit = False)
        product.user = request.user
        product.save()
        return redirect('main:show_main')

    context = {'form': form}
    return render(request, "create_product.html", context)

@login_required(login_url='/login')
def show_product(request, id):
    product = get_object_or_404(Product, pk=id)
    product.increment_views()

    context = {
        'product': product
    }

    return render(request, "product_detail.html", context)


def show_xml(request):
     product_list = Product.objects.all()
     xml_data = serializers.serialize("xml", product_list)
     return HttpResponse(xml_data, content_type="application/xml")

def show_json(request):
    product_list = Product.objects.all()
    data = [
        {
            'id': str(product.id),
            'name': product.name,
            'description': product.description,
            'price': product.price,
            'category': product.category,
            'thumbnail': product.thumbnail,
            'item_views': product.item_views,
            'updated_at': product.updated_at,
            'created_at': product.created_at.isoformat() if product.created_at else None,
            'is_featured': product.is_featured,
            'user_id': product.user_id,
        }
        for product in product_list
    ]

    return JsonResponse(data, safe=False)


def show_xml_by_id(request, product_id):
    try:
        product_item = Product.objects.filter(pk=product_id)
        xml_data = serializers.serialize("xml", product_item)
        return HttpResponse(xml_data, content_type="application/xml")
    except Product.DoesNotExist:
        return HttpResponse(status=404)

def show_json_by_id(request, product_id):
    try:
        product = Product.objects.select_related('user').get(pk=product_id)
        product.increment_views()

        data = {
            'id': str(product.id),
            'name': product.name,
            'description': product.description,
            'price': product.price,
            'category': product.category,
            'thumbnail': product.thumbnail,
            'item_views': product.item_views,
            'updated_at': product.updated_at,
            'created_at': product.created_at.isoformat() if product.created_at else None,
            'is_featured': product.is_featured,
            'user_id': product.user_id,
            'user_username': product.user.username if product.user_id else None,
        }

        return JsonResponse(data)
    except Product.DoesNotExist:
        return JsonResponse({'detail': 'Not found'}, status=404)
    
def register(request):
    form = UserCreationForm()

    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Your account has been successfully created!')
            return redirect('main:login')
    context = {'form':form}
    return render(request, 'register.html', context)

def login_user(request):
   if request.method == 'POST':
      form = AuthenticationForm(data=request.POST)

      if form.is_valid():
        user = form.get_user()
        login(request, user)
        response = HttpResponseRedirect(reverse("main:show_main"))
        response.set_cookie('last_login', str(datetime.datetime.now()))
        return response

   else:
      form = AuthenticationForm(request)
   context = {'form': form}
   return render(request, 'login.html', context)

def logout_user(request):
    logout(request)
    response = HttpResponseRedirect(reverse('main:login'))
    response.delete_cookie('last_login')
    return response

def edit_product(request, id):
    products = get_object_or_404(Product, pk=id)
    form = ProductForm(request.POST or None, instance=products)
    if form.is_valid() and request.method == 'POST':
        form.save()
        return redirect('main:show_main')

    context = {
        'form': form,
        'product': products
    }

    return render(request, "edit_product.html", context)

def delete_product(request, id):
    products = get_object_or_404(Product, pk=id)
    products.delete()
    return HttpResponseRedirect(reverse('main:show_main'))

@csrf_exempt
@require_POST
def add_product_entry_ajax(request):
    name = strip_tags(request.POST.get("name"))  # strip HTML tags!
    description = strip_tags(request.POST.get("description"))  # strip HTML tags!
    price = request.POST.get("price")
    category = request.POST.get("category")
    thumbnail = request.POST.get("thumbnail")
    is_featured = request.POST.get("is_featured") == 'on'  # checkbox handling
    user = request.user

    # Server-side validation for price
    try:
        price_float = float(price) if price else 0.0
        if price_float <= 0:
            return HttpResponse(b"INVALID_PRICE", status=400)
    except (ValueError, TypeError):
        return HttpResponse(b"INVALID_PRICE", status=400)

    new_product = Product(
        name=name,
        description=description,
        price=price,
        category=category,
        thumbnail=thumbnail,
        is_featured=is_featured,
        user=user
    )
    new_product.save()

    return HttpResponse(b"CREATED", status=201)

@csrf_exempt
@require_POST
def edit_product_entry_ajax(request, id):
    product = get_object_or_404(Product, pk=id)

    # Check if user owns the product
    if product.user != request.user:
        return HttpResponse(b"FORBIDDEN", status=403)

    name = strip_tags(request.POST.get("name"))  # strip HTML tags!
    description = strip_tags(request.POST.get("description"))  # strip HTML tags!
    price = request.POST.get("price")
    category = request.POST.get("category")
    thumbnail = request.POST.get("thumbnail")
    is_featured = request.POST.get("is_featured") == 'on'  # checkbox handling

    # Server-side validation for price
    try:
        price_float = float(price) if price else 0.0
        if price_float <= 0:
            return HttpResponse(b"INVALID_PRICE", status=400)
    except (ValueError, TypeError):
        return HttpResponse(b"INVALID_PRICE", status=400)

    product.name = name
    product.description = description
    product.price = price
    product.category = category
    product.thumbnail = thumbnail
    product.is_featured = is_featured
    product.save()

    return HttpResponse(b"UPDATED", status=200)

def proxy_image(request):
    image_url = request.GET.get('url')
    if not image_url:
        return HttpResponse('No URL provided', status=400)
    
    try:
        # Fetch image from external source
        response = requests.get(image_url, timeout=10)
        response.raise_for_status()
        
        # Return the image with proper content type
        return HttpResponse(
            response.content,
            content_type=response.headers.get('Content-Type', 'image/jpeg')
        )
    except requests.RequestException as e:
        return HttpResponse(f'Error fetching image: {str(e)}', status=500)