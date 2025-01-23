from email import message
from os import name
from django.db import transaction
from django.forms import ValidationError
from django.shortcuts import render
from baskets.models import Basket
from orders.models import Order, OrderItem
from django.contrib import messages
from django.shortcuts import redirect
from django.db.models import F

from orders.forms import CreateOrderForm


# Create your views here.
def create_order(request):
    if request.method == "POST":
        form = CreateOrderForm(data=request.POST)
        if form.is_valid():
            try:
                with transaction.atomic():
                    user = request.user
                    basket_items = Basket.objects.filter(user=user)

                    if basket_items.exists():
                        order = Order.objects.create(
                            user=user,
                            phone_number=form.cleaned_data["phone_number"],
                        )

                        for basket_item in basket_items:
                            product = basket_item.product
                            name = basket_item.product.name
                            price = basket_item.product.sell_price()
                            quantity = basket_item.quantity

                            if product.quantity < quantity or product.quantity == 0:
                                raise ValidationError(
                                    f"Недостаточно товара на складе{name}\ В наличии - {product.quantity}"
                                )

                            OrderItem.objects.create(
                                order=order,
                                product=product,
                                name=name,
                                price=price,
                                quantity=quantity,
                            )
                            product.quantity = F("quantity") - quantity
                            product.save()

                        basket_items.delete()

                        messages.success(request, "Заказ успешно оформлен")
                        return redirect("user:profile")
            except ValidationError as e:
                messages.error(request, str(e))
                context = {"title": "Home - Заказ", "form": form}
                return render(request, "orders/create_order.html", context=context)
            except Exception as e:
                messages.error(request, "Произошла ошибка при оформлении заказа.")
                context = {"title": "Home - Заказ", "form": form}
                return render(request, "orders/create_order.html", context=context)
        else:
            messages.error(request, "Некорректные данные в форме.")
    else:
        initial = {
            "first_name": request.user.first_name,
            "last_name": request.user.last_name,
        }
        form = CreateOrderForm(initial=initial)
    context = {"title": "Home - Заказ", "form": form}
    return render(request, "orders/create_order.html", context=context)
