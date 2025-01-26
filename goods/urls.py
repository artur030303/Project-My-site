
from django.urls import path

from goods import views

app_name = "goods"# имя приложения для маршрутизации

urlpatterns = [
    path("search/",
         views.CatalogView.as_view(), # представление, которое обрабатывает запрос на добавление товара в корзину(класс-based view)
         name="search"),# имя для ссылки на этот маршрут в шаблонах
    path("<slug:category_slug>/", views.CatalogView.as_view(), name="index"),
    path("product/<slug:product_slug>/", views.ProductView.as_view(), name="product"),
]
