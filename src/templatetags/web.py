from django import template

register = template.Library()



@register.simple_tag
def renderCartQuantity(request):
    cart = request.session.get("cart",[])
    count = 0
    for item in cart:
        count = count + item.get("quantity",0)
    return count