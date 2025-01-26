from django.db import models
from goods.models import Products
from users.models import User

# Create your models here.


# Это кастомный набор запросов для модели Basket, позволяющий добавлять методы, которые можно вызывать для QuerySet
class BasketQueryset(models.QuerySet):

    # Вычисляет общую стоимость всех товаров в корзине
    def total_price(self):
        return sum(basket.products_price() for basket in self)

    # Вычисляет общее количество всех товаров в корзине
    def total_quantity(self):
        if self:
            return sum(basket.quantity for basket in self)
        return 0


# Модель корзины
class Basket(models.Model):
    # связь корзины с пользователем.
    user = models.ForeignKey(
        to=User,  # ссылка на модель User
        on_delete=models.CASCADE,  # если пользователь удаляется, удаляется и его корзина.
        blank=True,
        null=True,  # поле может быть пустым, что позволяет использовать корзину без авторизации (например, для гостей).
        verbose_name="Пользователь",  # название поля в админке
    )
    # связь корзины с конкретным товаром
    product = models.ForeignKey(
        to=Products, on_delete=models.CASCADE, verbose_name="Товар"
    )
    # хранит количество добавленного товара.
    quantity = models.PositiveSmallIntegerField(  # Только положительные значения
        default=0, verbose_name="Количество"
    )
    # хранения сессии гостей (не авторизованных пользователей).
    session_key = models.CharField(max_length=32, null=True, blank=True)
    # хранит время добавления в корзину
    created_timestamp = models.DateTimeField(
        auto_now_add=True, verbose_name="Дата добавления"
    )

    # Добавляем кастомный набор запросов
    class Meta:
        db_table = "basket"  # название таблицы
        verbose_name = "Корзина"  # название корзины
        verbose_name_plural = "Корзины"  # название корзины во множественном числе

    # Добавляем кастомный набор запросов, менеджер для модели
    objects = BasketQueryset().as_manager()

    # Вычисляет  стоимость товара
    def products_price(self):
        return round(
            self.product.sell_price() * self.quantity,
            2,  # округляет итоговую стоимость до двух знаков после запятой
        )

    # возвращает название корзины
    def __str__(self):

        return f"Корзина {self.user.username} | Товар {self.product.name} | Количество {self.quantity}"
