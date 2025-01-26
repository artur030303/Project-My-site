from django.db.models import Q

from goods.models import Products

from django.contrib.postgres.search import (
    SearchVector,
    SearchQuery,
    SearchRank,
    SearchHeadline,
)

# функция для поиска товаров по запросу
def q_search(query):# query - строка запроса, которую вводит пользователь
    if query.isdigit() and len(query) <= 5:# проверяем, является ли query строкой, состоящей только из цифр и меньше либо равно 5 символам(id)
        return Products.objects.filter(id=int(query))# преобразуем query в целое число (int(query)) и фильтруем записи в модели Products по полю id
    
    # если query не является цифрой, то выполняем поиск по названию и описанию товара
    vector = SearchVector("name", "description")# создаем вектор для поиска по названию и описанию товара
    query = SearchQuery(query)# преобразуем пользовательский запрос query в объект SearchQuery, который используется для сравнения с вектором поиска
    
    # добавляем поле rank, которое хранит ранг совпадения запроса с вектором поиска
    result = (
        Products.objects.annotate(rank=SearchRank(vector, query))
        .filter(rank__gt=0)# фильтруем записи, где ранг совпадения больше 0
        .order_by("-rank")# сортируем записи по убыванию ранга совпадения
    )

    # добавляем поле headline, которое хранит подсветку совпадения запроса с названием товара
    result = result.annotate(
        headline=SearchHeadline(
            "name",
            query,
            start_sel='<span style="background-color: yellow;">',# определение начала и конца подсветки совпадения запроса с названием товара
            stop_sel="</span>",
        )
    )

    # добавляем поле bodyline, которое хранит подсветку совпадения запроса с описанием товара
    result = result.annotate(
        bodyline=SearchHeadline(
            "description",
            query,
            start_sel='<span style="background-color: yellow;">',
            stop_sel="</span>",
        )
    )
    return result
