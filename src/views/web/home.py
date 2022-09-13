from pprint import pprint
from django.shortcuts import render
from django.http import JsonResponse, HttpResponse
from marshmallow import Schema, fields, ValidationError, INCLUDE, validate
from src.repositories import ContactRepository, ProductCategoryRepository
import requests
import shopify

# validation
class ContactSchema(Schema):
    fullname = fields.String(required=True, validate=validate.Length(min=1, max=255))
    email = fields.Email(required=True, validate=validate.Length(min=1, max=255))
    phone = fields.String(required=True, validate=validate.Length(min=10, max=11))
    subject = fields.String(required=True, validate=validate.Length(min=1, max=255))
    message = fields.String(required=True, validate=validate.Length(min=1, max=1000))


def index(request):

    # get products
    # response = requests.get(
    #     "https://agn-store-6765.myshopify.com/admin/api/2021-10/products.json",
    #     headers={
    #         "Content-Type": "application/json",
    #         "Accept": "application/json",
    #         "X-Shopify-Access-Token": "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",
    #     },
    # )

    # create product
    # response = requests.post(
    #     "https://agn-store-6765.myshopify.com/admin/api/2021-10/products.json",
    #     headers={
    #         "Content-Type": "application/json",
    #         "Accept": "application/json",
    #         "X-Shopify-Access-Token": "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",
    #     },
    #     json={
    #         "product": {
    #             "title": "Burton Custom Freestyle 151",
    #             "body_html": "<strong>Good snowboard!</strong>",
    #             "vendor": "Burton",
    #             "product_type": "Snowboard",
    #             "tags": ["Barnes & Noble", "Big Air", "John's Fav"],
    #         }
    #     },
    # )

    # pprint(response.json())

    # return JsonResponse(response.json(), safe=False)

    if request.method == "POST":
        try:
            ContactSchema().load(request.POST, unknown=INCLUDE)
        except ValidationError as err:
            return JsonResponse({"errors": err.messages}, status=400)

        contactRepository = ContactRepository()

        contactRepository.create(
            fullname=request.POST.get("fullname"),
            email=request.POST.get("email"),
            phone=request.POST.get("phone"),
            subject=request.POST.get("subject"),
            message=request.POST.get("message"),
        )

        return JsonResponse({}, status=200)

    productCategoryRepository = ProductCategoryRepository()
    productCategories = productCategoryRepository.getAllActiveWithRelated()
    return render(
        request,
        "web/pages/home.html",
        {"productCategories": productCategories},
    )
