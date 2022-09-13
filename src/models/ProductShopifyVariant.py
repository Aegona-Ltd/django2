from django.db import models

from src.models import ProductShopify, ProductShopifyImage


class ProductShopifyVariant(models.Model):
    product = models.ForeignKey(ProductShopify, on_delete=models.CASCADE)
    title = models.TextField(null=True)
    price = models.TextField(null=True)
    sku = models.TextField(null=True)
    position = models.IntegerField(default=0)
    inventory_policy = models.TextField(null=True)
    compare_at_price = models.TextField(null=True)
    fulfillment_service = models.TextField(null=True)
    inventory_management = models.TextField(null=True)
    option1 = models.TextField(null=True)
    option2 = models.TextField(null=True)
    option3 = models.TextField(null=True)
    created_at = models.TextField(null=True)
    updated_at = models.TextField(null=True)
    taxable = models.IntegerField(default=0)
    barcode = models.TextField(null=True)
    grams = models.IntegerField(default=0)
    image = models.ForeignKey(ProductShopifyImage, on_delete=models.RESTRICT,null=True)
    weight = models.FloatField(default=0)
    weight_unit = models.TextField(null=True)
    inventory_item_id = models.IntegerField(default=0)
    inventory_quantity = models.IntegerField(default=0)
    old_inventory_quantity = models.IntegerField(default=0)
    requires_shipping = models.IntegerField(default=0)
    admin_graphql_api_id = models.TextField(null=True)
    presentment_prices = models.TextField(null=True)
