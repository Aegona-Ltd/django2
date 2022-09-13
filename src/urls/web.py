from django.urls import path
from src.views.web import home, productDetail, cart

app_name = "web"
urlpatterns = [
    path("", home.index, name="home"),
    path("product/<slug>-<id>", productDetail.index, name="productDetail"),
    path(
        "product/ajax/add-to-cart",
        productDetail.addToCart,
        name="productDetail.addToCart",
    ),
    path("cart", cart.index, name="cart"),
    path("cart/remove-cart-item", cart.removeCartItem, name="cart.removeCartItem"),
]
