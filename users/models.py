from django.db import models

from django.contrib.auth.models import AbstractUser


# Create your models here.
class User(AbstractUser): # AbstractUser - абстрактная модель пользователя Django включает в себя все нужные поля для пользователя
    image = models.ImageField(
        upload_to="users_images", blank=True, null=True, verbose_name="Аватар") # Указывает, что загружаемые изображения будут сохраняться в папке users_images 
    phone_number = models.CharField(max_length=10, blank=True, null=True)

    class Meta:
        db_table = "user" # имя таблицы
        verbose_name = "Пользователя" # название модели
        verbose_name_plural = "Пользователи" # название модели во множественном числе
    
    # метод возвращает строковое представление объекта
    def __str__(self):
        return self.username
