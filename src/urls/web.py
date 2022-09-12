from django.urls import path
from src.views.web import home

app_name = "web"
urlpatterns = [
    path("", home.index, name="home"),
]
