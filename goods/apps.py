from django.apps import AppConfig

# конфигурация приложения Django
class GoodsConfig(AppConfig):
    default_auto_field = "django.db.models.BigAutoField"
    name = "goods"
    verbose_name = "Товары"
