from django.shortcuts import render
from django.http import JsonResponse
from marshmallow import Schema, fields, ValidationError, INCLUDE, validate
from src.repositories import ContactRepository, ProductCategoryRepository

# validation
class ContactSchema(Schema):
    fullname = fields.String(required=True, validate=validate.Length(min=1, max=255))
    email = fields.Email(required=True, validate=validate.Length(min=1, max=255))
    phone = fields.String(required=True, validate=validate.Length(min=10, max=11))
    subject = fields.String(required=True, validate=validate.Length(min=1, max=255))
    message = fields.String(required=True, validate=validate.Length(min=1, max=1000))


def index(request):
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
    productCategories = (
        productCategoryRepository.getAllActiveWithRelated()
    )
    return render(
        request,
        "web/pages/home.html",
        {"productCategories": productCategories},
    )
