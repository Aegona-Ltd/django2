from django.shortcuts import render
from src.repositories import repository


def index(request):
    UserClientRepository = repository("UserClientRepository")
    return render(
        request,
        "web/pages/home.html",
        {},
    )
