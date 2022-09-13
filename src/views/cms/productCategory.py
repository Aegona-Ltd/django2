from pprint import pprint
from django.http import JsonResponse
from django.shortcuts import render
from django.contrib.auth.models import Permission, Group
from marshmallow import Schema, fields, ValidationError, INCLUDE, validate
from src.repositories import ProductCategoryRepository
from django.contrib.auth.decorators import permission_required


# validation
class ValidateSchema(Schema):
    name = fields.String(required=True, validate=validate.Length(min=1, max=255))

@permission_required("src.view_productcategory")
def index(request):
    productCategoryRepository = ProductCategoryRepository()
    productCategories = productCategoryRepository.getAllOrderByIdDesc()
    return render(
        request,
        "cms/pages/productCategory/index.html",
        {"productCategories": productCategories},
    )

@permission_required("src.add_productcategory")
def create(request):
    if request.method == "POST":
        try:
            ValidateSchema().load(request.POST, unknown=INCLUDE)
        except ValidationError as err:
            return JsonResponse({"errors": err.messages}, status=400)

        productCategoryRepository = ProductCategoryRepository()
        productCategoryRepository.create(name=request.POST.get("name"))

        return JsonResponse(request.POST, status=200)

    return render(request, "cms/pages/productCategory/create.html", {})

@permission_required("src.change_productcategory")
def update(request, id):
    productCategoryRepository = ProductCategoryRepository()
    productCategory = productCategoryRepository.getOne(id=id)

    if request.method == "POST":
        try:
            ValidateSchema().load(request.POST, unknown=INCLUDE)
        except ValidationError as err:
            return JsonResponse({"errors": err.messages}, status=400)

        productCategoryRepository = ProductCategoryRepository()
        productCategoryRepository.update(id=id, name=request.POST.get("name"))

        return JsonResponse(request.POST, status=200)

    return render(
        request,
        "cms/pages/productCategory/update.html",
        {"productCategory": productCategory},
    )

@permission_required("src.delete_productcategory")
def delete(request):
    if request.method == "POST":
        try:
            productCategoryRepository = ProductCategoryRepository()
            productCategoryRepository.delete(id=request.POST.get("id"))
            return JsonResponse(request.POST, status=200)
        except:
            return JsonResponse({"errors": "fail"}, status=400)
