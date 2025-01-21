from email.mime import image
from pyexpat import model
from tabnanny import verbose
from django.db import models
from django.forms import CharField
from django.urls import reverse


# Create your models here.
class Categories(models.Model):
    name = models.CharField(max_length=150, unique=True, verbose_name="Название")
    slug = models.SlugField(
        max_length=200, unique=True, blank=True, null=True, verbose_name="URL"
    )

    class Meta:
        db_table = "category"
        verbose_name = "Категорию"
        verbose_name_plural = "Категории"

    def __str__(self):
        return self.name


class Products(models.Model):
    name = models.CharField(max_length=150, unique=True, verbose_name="Название")
    slug = models.SlugField(
        max_length=200, unique=True, blank=True, null=True, verbose_name="URL"
    )
    mileage = models.PositiveIntegerField(
        null=False, blank=False, default=0, verbose_name="Пробег (км)"
    )
    description = models.TextField(blank=True, null=True, verbose_name="Описание")
    full_description = models.TextField(
        blank=True, null=True, verbose_name="Полное описание"
    )
    image = models.ImageField(
        upload_to="goods_images", blank=True, null=True, verbose_name="Изображение"
    )
    image_slide1 = models.ImageField(
        upload_to="goods_images",
        blank=True,
        null=True,
        verbose_name="Изображение Слайд-1",
    )
    image_slide2 = models.ImageField(
        upload_to="goods_images",
        blank=True,
        null=True,
        verbose_name="Изображение Слайд-2",
    )
    image_slide3 = models.ImageField(
        upload_to="goods_images",
        blank=True,
        null=True,
        verbose_name="Изображение Слайд-3",
    )
    price = models.IntegerField(verbose_name="Цена")
    discount = models.DecimalField(
        default=0.000, max_digits=5, decimal_places=2, verbose_name="Скидка в %"
    )
    quantity = models.PositiveIntegerField(default=0, verbose_name="Количество")
    category = models.ForeignKey(
        to=Categories, on_delete=models.PROTECT, verbose_name="Категория"
    )

    class Meta:
        db_table = "product"
        verbose_name = "Продукт"
        verbose_name_plural = "Продукты"

    def __str__(self):
        return f"{self.name} Количество - {self.quantity}"

    def get_absolute_url(self):
        return reverse("catalog:product", kwargs={"product_slug": self.slug})

    def display_id(self):
        return f"{self.id:05}"

    def sell_price(self):
        if self.discount:
            return round(self.price - self.price * self.discount / 100)
        return self.price
