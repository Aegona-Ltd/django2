from pprint import pprint
from django.shortcuts import render
from django.http import JsonResponse
from src.repositories import ContactRepository, ProductRepository
from django.forms import model_to_dict
from src.repositories import ProductShopifyRepository


def index(request,slug,id):
    productShopifyRepository = ProductShopifyRepository()
    product = productShopifyRepository.getOne(id=id)

    return render(
        request,
        "web/pages/productShopifyDetail.html",
        {"product": product},
    )