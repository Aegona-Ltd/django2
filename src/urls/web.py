from django.urls import path
from src.views.web import home, productDetail, cart,productShopify,productShopifyDetail

app_name = "web"
urlpatterns = [
    path("", productShopify.index, name="home"),
    path("product/<slug>-<id>", productDetail.index, name="productDetail"),
    path(
        "product/ajax/add-to-cart",
        productDetail.addToCart,
        name="productDetail.addToCart",
    ),
    path("cart", cart.index, name="cart"),
    path("cart/remove-cart-item", cart.removeCartItem, name="cart.removeCartItem"),
    path("cart/order", cart.order, name="cart.order"),

    path("product-shopify", productShopify.index, name="productShopify"),
    path("product-shopify/<slug>-<id>", productShopifyDetail.index, name="productShopifyDetail"),
    path(
        "product-shopify/ajax/add-to-cart",
        productShopifyDetail.addToCart,
        name="productShopifyDetail.addToCart",
    ),

    
]
