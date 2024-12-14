from turtle import title
from unicodedata import category
from django.http import HttpResponse
from django.shortcuts import render

from goods.models import Categories


def index(request):

    categories = Categories.objects.all()

    context = {"categories": categories}

    return render(request, "main/index.html", context)


def about(request):
    return render(request, "main/about_us.html")


def basket(request) -> HttpResponse:
    return render(request, "main/basket.html")
