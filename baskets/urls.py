from django.urls import path

from baskets import views

app_name = "baskets"# имя приложения для маршрутизации

urlpatterns = [
    path(
        "basket_add/<slug:product_slug>/",  #  маршрут принимает переменную product_slug, которая используется для идентификации добавляемого товара
        views.BasketAddView.as_view(),  #  представление, которое обрабатывает запрос на добавление товара в корзину(класс-based view)
        name="basket_add",  #  имя для ссылки на этот маршрут в шаблонах
    ),
    path("basket_change/<int:basket_id>/",views.BasketChangeView.as_view(),name="basket_change",),
    path("basket_remove/<int:basket_id>/",views.BasketRemoveView.as_view(),name="basket_remove",),
]
