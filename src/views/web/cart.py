from pprint import pprint
from django.shortcuts import render
from django.http import JsonResponse
from src.repositories import ContactRepository, ProductRepository
from django.forms import model_to_dict


def index(request):
    productRepository = ProductRepository()
    cart = request.session.get("cart", [])
    cartItems = []

    for (index, item) in enumerate(cart):
        product = productRepository.getOne(id=item.get("productId"), is_active=1)
        if product:
            cartItems.append({"quantity": item.get("quantity"), "product": product})

    pprint(cartItems)
    # return JsonResponse(cartItems,safe=False)
    return render(
        request,
        "web/pages/cart.html",
        {"cart": cartItems},
    )


def removeCartItem(request):
    cart = request.session.get("cart", [])
    cartItem, index = next(
        (
            [item, index]
            for (index, item) in enumerate(cart)
            if item["productId"] == request.POST.get("productId", 0)
        ),
        [None, None],
    )

    if cartItem:
        del cart[index]

    request.session["cart"] = cart

    return JsonResponse({"cart":cart}, safe=False)
