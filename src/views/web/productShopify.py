from pprint import pprint
from django.shortcuts import render
from django.http import JsonResponse
from src.repositories import ContactRepository, ProductRepository
from django.forms import model_to_dict
from src.repositories import ProductShopifyRepository


def index(request):
    productShopifyRepository = ProductShopifyRepository()
    products = productShopifyRepository.getAllOrderByIdDesc().prefetch_related('productshopifyvariant_set')

    return render(
        request,
        "web/pages/productShopify.html",
        {"products": products},
    )
