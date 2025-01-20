from django.shortcuts import render
from goods.models import Products
from baskets.models import Basket
from django.shortcuts import redirect


def basket_add(request, product_slug):

    product = Products.objects.get(slug=product_slug)

    if request.user.is_authenticated:
        baskets = Basket.objects.filter(user=request.user, product=product)

        if baskets.exists():
            basket = baskets.first()
            if basket:
                basket.quantity += 1
                basket.save()
        else:
            Basket.objects.create(user=request.user, product=product, quantity=1)
    return redirect(request.META["HTTP_REFERER"])


def basket_change(request, basket_id):
    if request.method == "POST":
        basket = Basket.objects.get(id=basket_id, user=request.user)
        action = request.POST.get("action")

        if action == "increment":
            basket.quantity += 1
        elif action == "decrement" and basket.quantity > 1:
            basket.quantity -= 1
        basket.save()
    return redirect(request.META.get("HTTP_REFERER", "/"))


def basket_remove(request, basket_id):
    basket = Basket.objects.get(id=basket_id)
    basket.delete()
    return redirect(request.META["HTTP_REFERER"])
