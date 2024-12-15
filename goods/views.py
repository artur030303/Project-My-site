from turtle import title
from django.http import HttpResponse
from django.shortcuts import render

from django.core.paginator import Paginator
from goods.models import Products


# Create your views here.
def catalog(request) -> HttpResponse:

    goods = Products.objects.all()

    paginator = Paginator(goods, 3)
    page_number = request.GET.get("page")
    page_obj = paginator.get_page(page_number)

    return render(request, "goods/catalog.html", {"page_obj": page_obj})


def product(request):
    return render(request, "goods/product.html")
