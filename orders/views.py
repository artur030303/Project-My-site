from email import message
from os import name
from django.db import transaction
from django.forms import ValidationError
from django.urls import reverse_lazy # генерирует URL для перенаправления, но откладывает вычисление до момента выполнения
from django.views.generic import FormView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render
from baskets.models import Basket
from orders.models import Order, OrderItem
from django.contrib import messages
from django.shortcuts import redirect
from django.db.models import F


from orders.forms import CreateOrderForm


# класс-представление для создания заказа LoginRequiredMixin позволяет защитить страницу от неавторизованных пользователей
class CreateOrderView(LoginRequiredMixin, FormView):
    template_name = "orders/create_order.html" # путь к HTML-шаблону
    form_class = CreateOrderForm # класс формы
    success_url = reverse_lazy("users:profile") #reverse_lazy генерирует URL для перенаправления, но откладывает вычисление до момента выполнения

    # метод возвращает начальные значения полей формы(предзаполняет форму данными из профиля пользователя (имя и фамилия))
    def get_initial(self):
        initial = super().get_initial()
        initial["first_name"] = self.request.user.first_name
        initial["last_name"] = self.request.user.last_name
        return initial
    
    # метод обрабатывает POST-запросы(валидация и сохранение заказа)
    def form_valid(self, form):
        try:
            with transaction.atomic(): # транзакция
                user = self.request.user # пользователь
                basket_items = Basket.objects.filter(user=user) # товары в корзине из бд

                if basket_items.exists(): # если товары есть в корзине
                    order = Order.objects.create( # создается новый заказ
                        user=user,
                        phone_number=form.cleaned_data["phone_number"],
                    )

                    for basket_item in basket_items: # цикл по каждому товару в корзине
                        product = basket_item.product # товар
                        name = basket_item.product.name # название
                        price = basket_item.product.sell_price() # цена
                        quantity = basket_item.quantity # количество

                        if product.quantity < quantity or product.quantity == 0: # если товара нет в наличии
                            # вызывает ValidationError
                            raise ValidationError(
                                f"Недостаточно товара на складе{name}\ В наличии - {product.quantity}"
                            )
                        
                        # cоздает запись в OrderItem для каждого товара в корзине
                        OrderItem.objects.create(
                            order=order,
                            product=product,
                            name=name,
                            price=price,
                            quantity=quantity,
                        )
                        product.quantity = F("quantity") - quantity # уменьшает количество товара на складе на количество товара в корзине
                        product.save() # сохраняет изменения в бд 

                    basket_items.delete() # удаляет товары из корзины после оформления заказа

                    messages.success(self.request, "Заказ успешно оформлен") # сообщение об успешном оформлении заказа
                    return redirect("user:profile") # перенаправление на страницу профиля пользователя
        except ValidationError as e: # вызывает ValidationError в случае ошибки валидации формы 
            messages.error(self.request, str(e)) # выводит сообщение об ошибке
            context = {"title": "Home - Заказ", "form": form} # передает форму в шаблон
            return render(self.request, "orders/create_order.html", context=context) # отображает шаблон 
        except Exception as e: # в случае иных ошибок 
            messages.error(self.request, "Произошла ошибка при оформлении заказа.") # выводит сообщение об ошибке 
            print("Ошибка при оформлении заказа:", e) # выводит сообщение в консоли 
            context = {"title": "Home - Заказ", "form": form} # передает форму в шаблон 
            return render(self.request, "orders/create_order.html", context=context) # отображает шаблон
    
    # метод обрабатывает невалидную форму
    def form_invalid(self, form):
        messages.error(self.request, "Заполните все поля!") # выводит сообщение об ошибке
        return redirect("orders:create_order") # перенаправляет на страницу создания заказа
    
    # метод возвращает контекст
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs) # получает контекст от родительского класса CreateView
        context["title"] = "Home - Заказ" # заголовок страницы
        context["order"] = True # оформление заказа включено 
        return context
