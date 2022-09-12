from pprint import pprint
from django.http import JsonResponse
from django.shortcuts import render
from django.contrib.auth.models import Permission, Group
from src.repositories import ContactRepository


def index(request):
    contactRepository = ContactRepository()
    contacts = contactRepository.getAllOrderByIdDesc()
    return render(request, "cms/pages/contact/index.html", {"contacts": contacts})
