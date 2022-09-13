from pprint import pprint
from django.shortcuts import render
from django.http import JsonResponse
from src.repositories import ContactRepository, ProductRepository
from django.forms import model_to_dict
from src.repositories import ProductShopifyRepository


def index(request, slug, id):
    productShopifyRepository = ProductShopifyRepository()
    product = productShopifyRepository.getOne(id=id)

    return render(
        request,
        "web/pages/productShopifyDetail.html",
        {"product": product},
    )


def addToCart(request):
    if request.method == "POST":
        cart = request.session.get("cart", [])
        cartItem, index = next(
            (
                [item, index]
                for (index, item) in enumerate(cart)
                if item.get("variant_id") == request.POST.get("variant_id", 0)
            ),
            [None, None],
        )

        if not cartItem:
            cart.append({"variant_id": request.POST.get("variant_id", 0), "quantity": 1})
        else:
            cart[index] = {
                "variant_id": cartItem.get("variant_id", 0),
                "quantity": cartItem.get("quantity", 0) + 1,
            }

        request.session["cart"] = cart
        return JsonResponse({"cart": cart})
