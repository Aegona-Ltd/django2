from django.db import models
from src.models import ProductShopify


class ProductShopifyOption(models.Model):
    product = models.ForeignKey(ProductShopify, on_delete=models.CASCADE)
    name = models.TextField(null=True)
    position = models.IntegerField(default=0)
    values = models.TextField(null=True)
