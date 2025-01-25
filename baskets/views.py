from django.shortcuts import render
from goods.models import Products
from baskets.models import Basket
from django.shortcuts import redirect

from django.contrib.auth.mixins import LoginRequiredMixin
from django.views import View
from django.shortcuts import redirect, get_object_or_404
from django.http import HttpResponseForbidden
from django.contrib import messages


class BasketAddView(LoginRequiredMixin, View):
    def post(self, request, *args, **kwargs):
        product_slug = kwargs.get("product_slug")
        product = get_object_or_404(Products, slug=product_slug)
        basket = Basket.objects.filter(user=request.user, product=product).first()
        if basket:
            basket.quantity += 1
            basket.save()
        else:
            Basket.objects.create(user=request.user, product=product, quantity=1)
        return redirect(request.META.get("HTTP_REFERER", "/"))


class BasketChangeView(View):

    def post(self, request, basket_id):
        basket = get_object_or_404(Basket, id=basket_id, user=request.user)
        action = request.POST.get("action")
        if action == "increment":
            basket.quantity += 1
        elif action == "decrement" and basket.quantity > 1:
            basket.quantity -= 1
        else:
            return HttpResponseForbidden("Invalid action")
        basket.save()
        return redirect(request.META.get("HTTP_REFERER", "/"))


class BasketRemoveView(View):
    def post(self, request, basket_id):  # Параметр должен совпадать с маршрутом
        basket_item = get_object_or_404(Basket, id=basket_id)
        basket_item.delete()
        messages.success(request, "Товар удалён из корзины.")
        return redirect(request.META.get("HTTP_REFERER", "/"))
