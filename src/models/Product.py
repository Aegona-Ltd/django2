from django.db import models

from src.models.ProductCategory import ProductCategory


class Product(models.Model):
    product_category = models.ForeignKey(ProductCategory, on_delete=models.RESTRICT)
    name = models.CharField(max_length=255, null=True)
    image = models.TextField(null=True)
    description = models.CharField(max_length=255, null=True)
    price = models.IntegerField(default=0)
    is_active = models.IntegerField(default=1)
    created_at = models.DateTimeField(null=True, auto_now_add=True)
    updated_at = models.DateTimeField(null=True, auto_now=True)
