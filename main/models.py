import uuid
from django.db import models
from django.contrib.auth.models import User

class Product(models.Model):
    CATEGORY_CHOICES = [
        ("club_home", "Club Home"),
        ("club_away", "Club Away"),
        ("national", "National Team"),
        ("training", "Training"),
        ("other", "Other"),
    ]
    
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=200)
    description = models.TextField(blank=True, null=True)
    category = models.CharField(max_length=20, choices=CATEGORY_CHOICES, default='club_home')
    price = models.DecimalField(max_digits=10, help_text="Price in USD (e.g., 249.99)", decimal_places=2, default=249.99)
    thumbnail = models.URLField(help_text="URL gambar produk", blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    is_featured = models.BooleanField(default=False)
    item_views = models.PositiveIntegerField(default=0)

    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True) 

    # class Meta:
    #     indexes = [
    #         models.Index(fields=["is_featured"]),
    #         models.Index(fields=["category"]),
    #         models.Index(fields=["-created_at"]),
    #     ]
    #     ordering = ["-is_featured", "-created_at"]
    
    # def get_absolute_url(self):
    #     return reverse("product_detail", args=[self.pk])

    def __str__(self):
        return self.name

    @property
    def is_product_hot(self):
        return self.item_views > 20

    def increment_views(self):
        self.item_views += 1
        self.save()