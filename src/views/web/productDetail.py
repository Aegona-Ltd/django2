from django.shortcuts import render
from django.http import JsonResponse
from src.repositories import ContactRepository, ProductRepository
from django.forms import model_to_dict


def index(request, slug, id):
    productRepository = ProductRepository()
    product = productRepository.getOne(id=id)
    return render(
        request,
        "web/pages/productDetail.html",
        {"product": product},
    )


def addToCart(request):
    if request.method == "POST":
        cart = request.session.get("cart", [])
        cartItem, index = next(
            (
                [item, index]
                for (index, item) in enumerate(cart)
                if item["productId"] == request.POST.get("productId", 0)
            ),
            [None, None],
        )

        if not cartItem:
            cart.append({"productId": request.POST.get("productId", 0), "quantity": 1})
        else:
            cart[index] = {
                "productId": cartItem.get("productId", 0),
                "quantity": cartItem.get("quantity", 0) + 1,
            }

        request.session["cart"] = cart
        return JsonResponse({"cart": cart})
