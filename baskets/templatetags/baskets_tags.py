from django import template
from baskets.models import Basket

register = (
    template.Library()
)  # регистрация нового тега в библиотеке шаблонов. Все пользовательские теги и фильтры должны быть зарегистрированы


# получения корзин пользователя, отсортированных по категориям продуктов
@register.simple_tag()
def user_baskets(request):
    if request.user.is_authenticated:
        return Basket.objects.filter(user=request.user).order_by("product__category")
