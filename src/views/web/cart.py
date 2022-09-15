from pprint import pprint
from django.shortcuts import render
from django.http import JsonResponse
from src.repositories import (
    ContactRepository,
    ProductShopifyRepository,
    ProductShopifyVariantRepository,
)
from django.forms import model_to_dict
from marshmallow import Schema, fields, ValidationError, INCLUDE, validate
import requests


class OrderSchema(Schema):
    firstname = fields.String(required=True, validate=validate.Length(min=1, max=255))
    lastname = fields.String(required=True, validate=validate.Length(min=1, max=255))
    address = fields.String(required=True, validate=validate.Length(min=1, max=255))
    province = fields.String(required=True, validate=validate.Length(min=1, max=255))
    city = fields.String(required=True, validate=validate.Length(min=1, max=255))
    country = fields.String(required=True, validate=validate.Length(min=1, max=255))
    zip = fields.String(required=True, validate=validate.Length(min=1, max=255))
    email = fields.Email(required=True, validate=validate.Length(min=1, max=255))
    phone = fields.String(required=True, validate=validate.Length(min=10, max=11))


def index(request):
    productShopifyVariantRepository = ProductShopifyVariantRepository()
    cart = request.session.get("cart", [])
    cartItems = []
    total = 0

    for (index, item) in enumerate(cart):
        variant = productShopifyVariantRepository.getOne(id=item.get("variant_id"))
        if variant:
            cartItems.append({"quantity": item.get("quantity"), "variant": variant})
            total += int(item.get("quantity")) * int(variant.price)

    # return JsonResponse(cartItems,safe=False)
    return render(
        request,
        "web/pages/cart.html",
        {"cart": cartItems, "total": total},
    )


def removeCartItem(request):
    cart = request.session.get("cart", [])
    cartItem, index = next(
        (
            [item, index]
            for (index, item) in enumerate(cart)
            if item["variant_id"] == request.POST.get("variant_id", 0)
        ),
        [None, None],
    )

    if cartItem:
        del cart[index]

    request.session["cart"] = cart

    return JsonResponse({"cart": cart}, safe=False)


def order(request):
    try:
        OrderSchema().load(request.POST, unknown=INCLUDE)
    except ValidationError as err:
        return JsonResponse({"errors": err.messages}, status=400)

    cart = request.session.get("cart", [])

    if len(cart) < 1:
        return JsonResponse({"errors": {"error": ["Cart is empty"]}}, status=400)

    # create order
    response = requests.post(
        "https://agn-store-6765.myshopify.com/admin/api/2021-10/orders.json",
        headers={
            "Content-Type": "application/json",
            "Accept": "application/json",
            "X-Shopify-Access-Token": "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",
        },
        json={
            "order": {
                "line_items": cart,
                "customer": {
                    "first_name": request.POST.get("firstname"),
                    "last_name": request.POST.get("lastname"),
                    "email": request.POST.get("email"),
                },
                "billing_address": {
                    "first_name": request.POST.get("firstname"),
                    "last_name": request.POST.get("lastname"),
                    "address1": request.POST.get("address"),
                    "phone": request.POST.get("phone"),
                    "city": request.POST.get("city"),
                    "province": request.POST.get("province"),
                    "country": request.POST.get("country"),
                    "zip": request.POST.get("zip"),
                },
                "shipping_address": {
                    "first_name": request.POST.get("firstname"),
                    "last_name": request.POST.get("lastname"),
                    "address1": request.POST.get("address"),
                    "phone": request.POST.get("phone"),
                    "city": request.POST.get("city"),
                    "province": request.POST.get("province"),
                    "country": request.POST.get("country"),
                    "zip": request.POST.get("zip"),
                },
                "email": request.POST.get("email"),
                # "transactions": [{"kind": "sale", "status": "success", "amount": 50.0}],
                "financial_status": "pending",
                # "discount_codes": [{"code": request.POST.get("discountCode",""), "amount": "10.00", "type": "percentage" }],
            }
        },
    )
    response.raise_for_status()

    return JsonResponse(request.POST)
