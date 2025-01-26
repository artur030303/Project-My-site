from django.apps import AppConfig


# конфигурация приложения Django
class BasketsConfig(AppConfig):
    default_auto_field = "django.db.models.BigAutoField"
    name = "baskets"
    verbose_name = "Корзины"
