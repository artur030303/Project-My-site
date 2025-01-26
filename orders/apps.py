from django.apps import AppConfig


# конфигурация приложения Django
class OrdersConfig(AppConfig):
    default_auto_field = "django.db.models.BigAutoField"
    name = "orders"
    verbose_name = "Заказы"
