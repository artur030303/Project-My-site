from django.shortcuts import render
from goods.models import Products
from baskets.models import Basket
from django.shortcuts import redirect

from django.contrib.auth.mixins import LoginRequiredMixin
from django.views import View
from django.shortcuts import redirect, get_object_or_404
from django.http import HttpResponseForbidden
from django.contrib import messages


class BasketAddView(LoginRequiredMixin, View): # LoginRequiredMixin нужен для того что бы пользователь был авторизован,если пользователь не авторизован, его перенаправит на страницу входа
   
    # метод для обработки post запроса
    def post(self, request, *args, **kwargs):
        product_slug = kwargs.get("product_slug")  # извлекается product_slug из URL
        product = get_object_or_404(Products, slug=product_slug)  # Если товар не найден, возвращается ошибка 404
        basket = Basket.objects.filter(user=request.user, product=product).first()# проверка наличия товара в корзине
        if basket:# если товар уже есть в корзине
            basket.quantity += 1 # увеличивается количество на 1
            basket.save()# сохраняется изменения
        else:# если товара нет в корзине
            Basket.objects.create(user=request.user, product=product, quantity=1)# создается новый объект корзины
        return redirect(request.META.get("HTTP_REFERER", "/"))# перенаправление на предыдущую страницу, если заголовок отсутствует , "/" то на главную страницу


# класс для изменения количества товара в корзине
class BasketChangeView(View):

    def post(self, request, basket_id):
        basket = get_object_or_404(Basket, id=basket_id, user=request.user)# извлекается объект корзины с id равным basket_id, принадлежащий текущему пользователю
        action = request.POST.get("action")# извлекается значение action из POST запроса(пользователь нажал кнопку + или -)
        if action == "increment":
            basket.quantity += 1
            basket.save()
        elif action == "decrement": 
            if basket.quantity > 1:
               basket.quantity -= 1
               basket.save()
            else:
               messages.success(request, "Остался только один товар! Если хотите удалить товар полностью нажмите на значок корзины")    
        else:
            return HttpResponseForbidden("Invalid action")# если действие недопустимое, возвращается ошибка
        basket.save()# сохраняется изменения
        return redirect(request.META.get("HTTP_REFERER", "/"))# перенаправление на предыдущую страницу, без заголовка "/" на главную

# класс для удаления товара из корзины
class BasketRemoveView(View):
    def post(self, request, basket_id):  # Параметр должен совпадать с маршрутом
        basket_item = get_object_or_404(Basket, id=basket_id)# извлекается объект корзины с id равным basket_id, если объект не найден, возвращается ошибка
        basket_item.delete()# удаляется объект корзины
        messages.success(request, "Товар удалён из корзины.")# сообщение об успешном удалении
        return redirect(request.META.get("HTTP_REFERER", "/"))# перенаправление на предыдущую страницу, без заголовка "/" на главную
