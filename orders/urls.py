from django.urls import path

from orders import views

app_name = "orders" # имя приложения для маршрутизации 

urlpatterns = [
    path("create-order/", # маршрут
          views.CreateOrderView.as_view(), # представление, которое обрабатывает запрос на добавление товара в корзину(класс-based view)
          name="create_order") # имя для ссылки на этот маршрут в шаблонах
]
