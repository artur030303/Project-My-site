from django.http import HttpResponse
from django.shortcuts import render


def index(request):
    return render(request, "main/index.html")


def about(request):
    return render(request, "main/about_us.html")


def basket(request) -> HttpResponse:
    return render(request, "main/basket.html")
