from django.db import models

from goods.models import Products
from users.models import User


# Create your models here.

# класс предоставляет кастомные методы для работы с набором объектов OrderItem.
class OrderitemQueryset(models.QuerySet):
    
    # метод возвращает общую стоимость заказа
    def total_price(self):
        return sum(basket.products_price() for basket in self)
    
    # метод возвращает общее количество товаров
    def total_quantity(self):
        if self:
            return sum(cart.quantity for cart in self)
        return 0


# класс представляет модель заказа
class Order(models.Model):
    user = models.ForeignKey(# cвязь с моделью User через ForeignKey
        to=User,
        on_delete=models.SET_DEFAULT,# Когда объект, связанный через ForeignKey, удаляется, значение этого поля устанавливается в его значение по умолчанию, заданное через параметр default
        blank=True,
        null=True,
        verbose_name="Пользователь",
        default=None,
    )
    created_timestamp = models.DateTimeField(auto_now_add=True, verbose_name="Дата создания заказа")# дата и время создания
    phone_number = models.CharField(max_length=25, verbose_name="Номер телефона")# поле для хранения номера телефона покупател
    status = models.CharField(max_length=100, default="В обработке", verbose_name="Статус заказа")# cтатус заказа, значение по умолчанию — "В обработке"

    class Meta:
        db_table = "order" # название таблицы
        verbose_name = "Заказ" # название модели
        verbose_name_plural = "Заказы" # название модели во множественном числе
        ordering = ["-created_timestamp"] # сортировка по убыванию даты создания
    
    # метод возвращает строковое представление объекта
    def __str__(self):
        return f"Заказ № {self.pk} | Покупатель {self.user.first_name} {self.user.last_name}"
    
    # метод возвращает общую стоимость заказа
    def get_total_cost(self):
        return sum(item.get_cost() for item in self.orderitem_set.all())


# класс представляет модель товара в заказе
class OrderItem(models.Model): 
    order = models.ForeignKey(to=Order, on_delete=models.CASCADE, verbose_name="Заказ")# связь с моделью Order через ForeignKey, при удалении заказа удаляются и связанные товары(CASCADE)
    product = models.ForeignKey( # связь с моделью Products через ForeignKey
        to=Products,
        on_delete=models.SET_DEFAULT, # при удалении товара его значение заменяется на None(default=None)
        null=True,
        blank=True,
        verbose_name="Продукт",
        default=None,
    )
    name = models.CharField(max_length=200, verbose_name="Название")
    price = models.IntegerField(verbose_name="Цена")
    quantity = models.PositiveIntegerField(default=0, verbose_name="Количество")
    created_timestamp = models.DateTimeField(auto_now_add=True, verbose_name="Дата продажи" # дата и время продажи
    )

    # метод возвращает общую стоимость
    def get_cost(self):
        return self.price * self.quantity

    class Meta:
        db_table = "order_item"
        verbose_name = "Проданный товар"
        verbose_name_plural = "Проданные товары"

    objects = OrderitemQueryset.as_manager()

    # метод возвращает общую стоимость и округляет результат до двух знаков
    def products_price(self):
        return round(self.price * self.quantity, 2)
    
    # метод возвращает строковое представление объекта
    def __str__(self):
        return f"Товар {self.name} | Заказ № {self.order.pk}"
