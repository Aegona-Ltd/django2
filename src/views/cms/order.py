from django.http import JsonResponse
from django.shortcuts import render
from django.contrib.auth.decorators import login_required
import requests
from django.conf import settings
import graphene

def index(request):
    

    class Query(graphene.ObjectType):
        hello = graphene.String(name=graphene.String(default_value="World"))

    def resolve_hello(self, info, name):
        return 'Hello ' + name

    schema = graphene.Schema(query=Query)
    result = schema.execute('{ hello }')
    print(result.data['hello']) # "Hello World"


    response = requests.get(
        "https://%s.myshopify.com/admin/api/2021-10/orders.json?status=any"
        % (settings.SHOPIFY_STORE),
        headers={
            "Content-Type": "application/json",
            "Accept": "application/json",
            "X-Shopify-Access-Token": settings.SHOPIFY_ACCESS_TOKEN,
        },
    )

    orders = response.json().get("orders")
    # return JsonResponse(orders, safe=False)
    return render(request, "cms/pages/order/index.html", {"orders": orders})


def changeStatus(request):
    shop_url = "https://%s.myshopify.com/admin/api/2021-10" % (settings.SHOPIFY_STORE)
    order_id = request.POST.get("order_id")
    headers = {
        "Content-Type": "application/json",
        "Accept": "application/json",
        "X-Shopify-Access-Token": settings.SHOPIFY_ACCESS_TOKEN,
    }
    # get order fulfillment id
    res = requests.get(
        shop_url + "/orders/" + order_id + "/fulfillment_orders.json",
        headers={
            "Content-Type": "application/json",
            "Accept": "application/json",
            "X-Shopify-Access-Token": settings.SHOPIFY_ACCESS_TOKEN,
        },
    )

    res.raise_for_status()
    fulfillment_orders = res.json()

    fulfillment_id = fulfillment_orders["fulfillment_orders"][0]["id"]
    res = requests.get(shop_url + "/locations.json", headers=headers,)

    res.raise_for_status()
    location_id = res.json()["locations"][0]["id"]
    # get orders fulfillment line items

    # note: if you want to fulfill only certain products in the order with the tracking code,
    # here's where you select these products. Right now, the code isn't doing this

    fulfillment_order_line_items = []

    for item in fulfillment_orders["fulfillment_orders"][0]["line_items"]:

        fulfillment_order_line_items.append(
            {
                "id": item["id"],
                "quantity": item["quantity"],
            }
        )

    # set up payload
    payload = {
        "fulfillment": {
            "notify_customer": "false",
            "location_id": location_id,
            "tracking_info": {
                "url": "tracking_url",
                "company": "transport_company",
                "number": 1232,
            },
            "line_items_by_fulfillment_order": [
                {
                    "fulfillment_order_id": fulfillment_id,
                    "fulfillment_order_line_items": fulfillment_order_line_items,
                }
            ],
        }
    }

    # parse tracking info
    res = requests.post(
        shop_url + "/fulfillments.json",
        json=payload,
        headers=headers,
    )
    res.raise_for_status()
    return JsonResponse({}, safe=False)


def paid(request):
    # try:
    #     r = requests.post('somerestapi.com/post-here', data={'birthday': '9/9/3999'})
    #     r.raise_for_status()
    # except requests.exceptions.HTTPError as e:
    # print (e.response.text)

    response = requests.post(
        "https://%s.myshopify.com/admin/api/2022-07/orders/4656247308457/transactions.json"
        % (settings.SHOPIFY_STORE),
        headers={
            "Content-Type": "application/json",
            "Accept": "application/json",
            "X-Shopify-Access-Token": settings.SHOPIFY_ACCESS_TOKEN,
        },
        json={
            "transaction": {
                "currency": "VND",
                "amount": "1000",
                "kind": "capture",
                "parent_id": 389404469,
            }
        },
    )
    response.raise_for_status()
    orders = response.json()
    return JsonResponse({}, safe=False)
