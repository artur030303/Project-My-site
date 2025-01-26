from django.utils.http import urlencode
from django import template

from goods.models import Categories

register = template.Library()


@register.simple_tag()# регистрирует функцию как пользовательский тег, который можно использовать в шаблонах
def tag_categories():# функция которая возвращает список всех объектов модели Categories
    return Categories.objects.all()# запрос в базу данных

# принимает контекст шаблона (например, информацию о текущем запросе) через аргумент context
@register.simple_tag(takes_context=True)
def change_params(context, **kwargs):# функция, которая изменяет параметры запроса (GET)
    query = context["request"].GET.dict()# получаем словарь параметров запроса
    query.update(kwargs)# обновляем словарь новыми параметрами запроса переданными через kwargs
    return urlencode(query)# преобразуем обновленный словарь query в строку параметров запроса, используя функцию urlencode
