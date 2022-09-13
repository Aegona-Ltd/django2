from django.db import models
from src.models import ProductShopify

class ProductShopifyImage(models.Model):
    product = models.ForeignKey(ProductShopify, on_delete=models.CASCADE)
    position = models.IntegerField(default=0)
    created_at = models.TextField(null=True)
    updated_at = models.TextField(null=True)
    alt = models.TextField(null=True)
    width = models.IntegerField(default=0)
    height = models.IntegerField(default=0)
    src = models.TextField(null=True)
    variant_ids = models.TextField(null=True)
    admin_graphql_api_id = models.TextField(null=True)
