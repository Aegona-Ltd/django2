# Generated by Django 4.1 on 2022-09-13 07:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("src", "0003_alter_productshopifyvariant_image"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="productshopify",
            name="image_id",
        ),
        migrations.AddField(
            model_name="productshopify",
            name="image",
            field=models.TextField(null=True),
        ),
    ]