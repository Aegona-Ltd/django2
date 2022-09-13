from pprint import pprint
from django.http import JsonResponse
from django.shortcuts import render
from django.contrib.auth.models import Permission, Group
from marshmallow import Schema, fields, ValidationError, INCLUDE, validate
from src.repositories import ProductRepository, ProductCategoryRepository
from src.services.utilities.uploadFile import uploadFile, validateFile
from django.contrib.auth.decorators import permission_required


# validation
class ValidateSchema(Schema):
    product_category_id = fields.Integer(
        required=True, validate=validate.Range(min=1, max=10**20 - 1)
    )
    name = fields.String(required=True, validate=validate.Length(min=1, max=255))
    description = fields.String(required=True, validate=validate.Length(min=1, max=255))
    price = fields.Integer(
        required=True, validate=validate.Range(min=1, max=10**20 - 1)
    )
    is_active = fields.Integer(required=True, validate=validate.Range(min=0, max=1))


@permission_required("src.view_product")
def index(request):
    productRepository = ProductRepository()
    products = productRepository.getAllOrderByIdDesc()
    return render(
        request,
        "cms/pages/product/index.html",
        {"products": products},
    )

@permission_required("src.add_product")
def create(request):
    if request.method == "POST":
        try:
            ValidateSchema().load(request.POST, unknown=INCLUDE)
        except ValidationError as err:
            return JsonResponse({"errors": err.messages}, status=400)

        if "image" in request.FILES:
            return JsonResponse({"errors": {"image": ["File is required"]}}, status=400)
        error = validateFile(request.FILES["image"], "image", 10000000)
        if error:
            return JsonResponse({"errors": {"image": [error]}}, status=400)

        productRepository = ProductRepository()
        productRepository.create(
            product_category_id=request.POST.get("product_category_id"),
            name=request.POST.get("name"),
            description=request.POST.get("description"),
            price=request.POST.get("price"),
            is_active=request.POST.get("is_active"),
            image=uploadFile(request.FILES["image"], "/static/uploads/images/"),
        )

        return JsonResponse(request.POST, status=200)

    productCategoryRepository = ProductCategoryRepository()
    productCategories = productCategoryRepository.getAllOrderByIdDesc()
    return render(
        request,
        "cms/pages/product/create.html",
        {"productCategories": productCategories},
    )

@permission_required("src.change_product")
def update(request, id):
    productRepository = ProductRepository()
    product = productRepository.getOne(id=id)

    if request.method == "POST":
        try:
            ValidateSchema().load(request.POST, unknown=INCLUDE)
        except ValidationError as err:
            return JsonResponse({"errors": err.messages}, status=400)

        image = product.image
        if "image" in request.FILES:
            error = validateFile(request.FILES["image"], "image", 10000000)
            if error:
                return JsonResponse({"errors": {"image": [error]}}, status=400)
            image = uploadFile(request.FILES["image"], "/static/uploads/images/")

        productRepository = ProductRepository()
        productRepository.update(
            id = id,
            product_category_id=request.POST.get("product_category_id"),
            name=request.POST.get("name"),
            description=request.POST.get("description"),
            price=request.POST.get("price"),
            is_active=request.POST.get("is_active"),
            image=image,
        )

        return JsonResponse(request.POST, status=200)

    productCategoryRepository = ProductCategoryRepository()
    productCategories = productCategoryRepository.getAllOrderByIdDesc()
    return render(
        request,
        "cms/pages/product/update.html",
        {"productCategories": productCategories, "product": product},
    )

@permission_required("src.delete_product")
def delete(request):
    if request.method == "POST":
        try:
            productRepository = ProductRepository()
            productRepository.delete(id=request.POST.get("id"))
            return JsonResponse(request.POST, status=200)
        except:
            return JsonResponse({"errors": "fail"}, status=400)
