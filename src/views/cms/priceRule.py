from pprint import pprint
from django.http import JsonResponse
from django.shortcuts import render
from django.contrib.auth.decorators import login_required
import requests
from django.conf import settings

def index(request):
    #get priceRules
    response = requests.get(
        "https://%s.myshopify.com/admin/api/2021-10/price_rules.json" % (settings.SHOPIFY_STORE),
        headers={
            "Content-Type": "application/json",
            "Accept": "application/json",
            "X-Shopify-Access-Token": settings.SHOPIFY_ACCESS_TOKEN,
        },
    )

    priceRules = response.json()
    return JsonResponse(response.json())
    pprint(priceRules)

    return render(request, "cms/pages/priceRule/index.html", {"priceRules":priceRules})


def create(request):
    return render(request, "cms/pages/priceRule/create.html", {})


def update(request):
    return render(request, "cms/pages/priceRule/index.html", {})


def delete(request):
    return render(request, "cms/pages/priceRule/index.html", {})
