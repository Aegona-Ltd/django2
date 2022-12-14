# Generated by Django 4.1 on 2022-09-13 04:41

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Contact",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("fullname", models.CharField(max_length=255, null=True)),
                ("email", models.CharField(max_length=255, null=True)),
                ("phone", models.CharField(max_length=255, null=True)),
                ("subject", models.CharField(max_length=255, null=True)),
                ("message", models.TextField(null=True)),
                ("created_at", models.DateTimeField(auto_now_add=True, null=True)),
                ("updated_at", models.DateTimeField(auto_now=True, null=True)),
            ],
        ),
        migrations.CreateModel(
            name="ProductCategory",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("name", models.CharField(max_length=255, null=True)),
                ("created_at", models.DateTimeField(auto_now_add=True, null=True)),
                ("updated_at", models.DateTimeField(auto_now=True, null=True)),
            ],
        ),
        migrations.CreateModel(
            name="ProductShopify",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("title", models.TextField(null=True)),
                ("body_html", models.TextField(null=True)),
                ("vendor", models.TextField(null=True)),
                ("product_type", models.TextField(null=True)),
                ("created_at", models.TextField(null=True)),
                ("handle", models.TextField(null=True)),
                ("updated_at", models.TextField(null=True)),
                ("published_at", models.TextField(null=True)),
                ("template_suffix", models.TextField(null=True)),
                ("status", models.TextField(null=True)),
                ("published_scope", models.TextField(null=True)),
                ("tags", models.TextField(null=True)),
                ("admin_graphql_api_id", models.TextField(null=True)),
                ("image_id", models.IntegerField(default=0)),
            ],
        ),
        migrations.CreateModel(
            name="ProductShopifyImage",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("position", models.IntegerField(default=0)),
                ("created_at", models.TextField(null=True)),
                ("updated_at", models.TextField(null=True)),
                ("alt", models.TextField(null=True)),
                ("width", models.IntegerField(default=0)),
                ("height", models.IntegerField(default=0)),
                ("src", models.TextField(null=True)),
                ("variant_ids", models.TextField(null=True)),
                ("admin_graphql_api_id", models.TextField(null=True)),
                (
                    "product",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="src.productshopify",
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="UserClient",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("email", models.CharField(max_length=255, unique=True)),
                ("password", models.CharField(max_length=255, null=True)),
                ("name", models.CharField(max_length=255, null=True)),
                ("created_at", models.DateTimeField(auto_now_add=True, null=True)),
                ("updated_at", models.DateTimeField(auto_now=True, null=True)),
            ],
        ),
        migrations.CreateModel(
            name="ProductShopifyVariant",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("title", models.TextField(null=True)),
                ("price", models.TextField(null=True)),
                ("sku", models.TextField(null=True)),
                ("position", models.IntegerField(default=0)),
                ("inventory_policy", models.TextField(null=True)),
                ("compare_at_price", models.TextField(null=True)),
                ("fulfillment_service", models.TextField(null=True)),
                ("inventory_management", models.TextField(null=True)),
                ("option1", models.TextField(null=True)),
                ("option2", models.TextField(null=True)),
                ("option3", models.TextField(null=True)),
                ("created_at", models.TextField(null=True)),
                ("updated_at", models.TextField(null=True)),
                ("taxable", models.IntegerField(default=0)),
                ("barcode", models.TextField(null=True)),
                ("grams", models.IntegerField(default=0)),
                ("weight", models.FloatField(default=0)),
                ("weight_unit", models.TextField(null=True)),
                ("inventory_item_id", models.IntegerField(default=0)),
                ("inventory_quantity", models.IntegerField(default=0)),
                ("old_inventory_quantity", models.IntegerField(default=0)),
                ("requires_shipping", models.IntegerField(default=0)),
                ("admin_graphql_api_id", models.TextField(null=True)),
                ("presentment_prices", models.TextField(null=True)),
                (
                    "image",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.RESTRICT,
                        to="src.productshopifyimage",
                    ),
                ),
                (
                    "product",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="src.productshopify",
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="ProductShopifyOption",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("name", models.TextField(null=True)),
                ("position", models.IntegerField(default=0)),
                ("values", models.TextField(null=True)),
                (
                    "product",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="src.productshopify",
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="Product",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("name", models.CharField(max_length=255, null=True)),
                ("image", models.TextField(null=True)),
                ("description", models.CharField(max_length=255, null=True)),
                ("price", models.IntegerField(default=0)),
                ("is_active", models.IntegerField(default=1)),
                ("created_at", models.DateTimeField(auto_now_add=True, null=True)),
                ("updated_at", models.DateTimeField(auto_now=True, null=True)),
                (
                    "product_category",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.RESTRICT,
                        to="src.productcategory",
                    ),
                ),
            ],
        ),
    ]
