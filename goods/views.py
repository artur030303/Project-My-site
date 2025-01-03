from turtle import title
from unicodedata import category
from django.http import HttpResponse
from django.shortcuts import render

from django.core.paginator import Paginator
from goods.models import Products
from goods.utils import q_search


# Create your views here.
def catalog(request, category_slug=None) -> HttpResponse:

    page_number = request.GET.get("page")
    on_sale = request.GET.get("on_sale", None)
    order_by = request.GET.get("order_by", None)
    query = request.GET.get("q", None)

    if category_slug == "all":
        goods = Products.objects.all()
    elif query:
        goods = q_search(query)
    else:
        goods = Products.objects.filter(category__slug=category_slug)

    if on_sale:
        goods = goods.filter(discount__gt=0)

    if order_by and order_by != "default":
        goods = goods.order_by(order_by)

    paginator = Paginator(goods, 3)
    page_obj = paginator.get_page(page_number)

    context = {
        "page_obj": page_obj,
        "goods": goods,
        "on_sale": on_sale,
        "order_by": order_by,
        "slug_url": category_slug,
    }

    return render(request, "goods/catalog.html", context)


def product(request, product_slug):
    product = Products.objects.get(slug=product_slug)

    context = {"product": product}
    return render(request, "goods/product.html", context=context)
