from django.db import models


class ProductShopify(models.Model):
    title = models.TextField(null=True)
    body_html = models.TextField(null=True)
    vendor = models.TextField(null=True)
    product_type = models.TextField(null=True)
    created_at = models.TextField(null=True)
    handle = models.TextField(null=True)
    updated_at = models.TextField(null=True)
    published_at = models.TextField(null=True)
    template_suffix = models.TextField(null=True)
    status = models.TextField(null=True)
    published_scope = models.TextField(null=True)
    tags = models.TextField(null=True)
    admin_graphql_api_id = models.TextField(null=True)
    image = models.TextField(null=True)
    
