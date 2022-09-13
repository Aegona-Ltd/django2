import json
from turtle import title
from django.http import HttpResponse, JsonResponse
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
import requests
from src.repositories import (
    ProductShopifyRepository,
    ProductShopifyImageRepository,
    ProductShopifyVariantRepository,
    ProductShopifyOptionRepository,
)
from django.urls import reverse


def index(request):
    productShopifyRepository = ProductShopifyRepository()
    products = productShopifyRepository.getAllOrderByIdDesc()
    return render(
        request, "cms/pages/productShopify/index.html", {"products": products}
    )


def sync(request):

    productShopifyRepository = ProductShopifyRepository()
    productShopifyImageRepository = ProductShopifyImageRepository()
    productShopifyVariantRepository = ProductShopifyVariantRepository()
    productShopifyOptionRepository = ProductShopifyOptionRepository()

    # get products
    response = requests.get(
        "https://agn-store-6765.myshopify.com/admin/api/2021-10/products.json",
        headers={
            "Content-Type": "application/json",
            "Accept": "application/json",
            "X-Shopify-Access-Token": "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",
        },
    )

    resProducts = response.json().get("products")

    for resProduct in resProducts:
        image = resProduct.get("image")
        images = resProduct.get("images")
        options = resProduct.get("options")
        variants = resProduct.get("variants")

        for option in options:
            productShopifyOptionRepository.updateOrCreate(
                id=option.get("id"),
                product_id=option.get("product_id"),
                name=option.get("name"),
                position=option.get("position"),
                values=json.dumps(option.get("values")),
            )

        for variant in variants:
            productShopifyVariantRepository.updateOrCreate(
                id=variant.get("id"),
                product_id=variant.get("product_id"),
                title=variant.get("title"),
                price=variant.get("price"),
                sku=variant.get("sku"),
                position=variant.get("position"),
                inventory_policy=variant.get("inventory_policy"),
                compare_at_price=variant.get("compare_at_price"),
                fulfillment_service=variant.get("fulfillment_service"),
                inventory_management=variant.get("inventory_management"),
                option1=variant.get("option1"),
                option2=variant.get("option2"),
                option3=variant.get("option3"),
                created_at=variant.get("created_at"),
                updated_at=variant.get("updated_at"),
                taxable=variant.get("taxable"),
                barcode=variant.get("barcode"),
                grams=variant.get("grams"),
                image_id=variant.get("image_id"),
                weight=variant.get("weight"),
                weight_unit=variant.get("weight_unit"),
                inventory_item_id=variant.get("inventory_item_id"),
                inventory_quantity=variant.get("inventory_quantity"),
                old_inventory_quantity=variant.get("old_inventory_quantity"),
                requires_shipping=variant.get("requires_shipping"),
                admin_graphql_api_id=variant.get("admin_graphql_api_id"),
            )

        for img in images:
            productShopifyImageRepository.updateOrCreate(
                id=img.get("id"),
                product_id=img.get("product_id"),
                position=img.get("position"),
                created_at=img.get("created_at"),
                updated_at=img.get("updated_at"),
                alt=img.get("alt"),
                width=img.get("width"),
                height=img.get("height"),
                src=img.get("src"),
                variant_ids=json.dumps(img.get("variant_ids")),
                admin_graphql_api_id=img.get("admin_graphql_api_id"),
            )

        productShopifyRepository.updateOrCreate(
            id=resProduct.get("id"),
            title=resProduct.get("title"),
            body_html=resProduct.get("body_html"),
            vendor=resProduct.get("vendor"),
            product_type=resProduct.get("product_type"),
            created_at=resProduct.get("created_at"),
            updated_at=resProduct.get("updated_at"),
            handle=resProduct.get("handle"),
            published_at=resProduct.get("published_at"),
            template_suffix=resProduct.get("template_suffix"),
            status=resProduct.get("status"),
            published_scope=resProduct.get("published_scope"),
            tags=resProduct.get("tags"),
            admin_graphql_api_id=resProduct.get("admin_graphql_api_id"),
            image=image.get("src"),
        )

    # return JsonResponse(resProducts, safe=False)
    return redirect(reverse("cms:productShopify.index"))
