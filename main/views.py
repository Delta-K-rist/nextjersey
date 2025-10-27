from django.shortcuts import render

def show_main(request):
    context = {
        'npm' : '2406425810',
        'name': 'Deltakristiano Kurniaputra',
        'class': 'PBP C'
    }

    return render(request, "main.html", context)