from turtle import title

from django.template import context
from django.views.generic import DetailView, ListView
from goods.models import Products
from goods.utils import q_search


# класс для отображения каталога 
class CatalogView(ListView):
    model = Products # этот ListView работает с моделью Products
    template_name = "goods/catalog.html" # шаблон каталога
    context_object_name = "goods" # имя переменной в шаблоне каталога
    paginate_by = 3 # пагинация на 3 товара
    
    # получение параметров запроса
    def get_queryset(self):
        category_slug = self.kwargs.get("category_slug")# извлекается category_slug из URL
        on_sale = self.request.GET.get("on_sale")# проверяем, передан ли в запросе параметр on_sale, фильтр для товаров со скидкой
        order_by = self.request.GET.get("order_by")# проверяем если передан параметр order_by, сортировка товаров
        query = self.request.GET.get("q")#  строка поискового запроса (если пользователь что-то ищет)

        if category_slug == "all":
            goods = super().get_queryset()# получаем все товары
        elif query:
            goods = q_search(query)# получаем результаты поиска
        else:
            goods = super().get_queryset().filter(category__slug=category_slug)# получаем товары только из выбранной категории

        if on_sale:
            goods = goods.filter(discount__gt=0)# фильтруем товары со скидкой

        if order_by and order_by != "default":
            goods = goods.order_by(order_by)# сортируем товары
        return goods
    
    # получение контекста
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)# получаем базовый контекст от родительского класса ListView
        context["title"] = "Home - Каталог"# заголовок страницы
        context["slug_url"] = self.kwargs.get("category_slug")# в контекст добавляется slug текущей категории для использования в шаблоне.
        return context


# класс для отображения товара
class ProductView(DetailView):
    template_name = "goods/product.html"# шаблон для отображения товара
    slug_url_kwarg = "product_slug"# переменная для идентификации товара в URL
    context_object_name = "product"# имя переменной в шаблоне
    
    # получение объекта
    def get_object(self, queryset=None):
        product = Products.objects.get(slug=self.kwargs.get(self.slug_url_kwarg))# получаем продукт из базы данных по значению slug, которое передается через параметр product_slug в URL.
        return product
    
    # получение контекста
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)# получаем базовый контекст от родительского класса DetailView
        context["title"] = self.object.name # заголовок страницы
        return context
