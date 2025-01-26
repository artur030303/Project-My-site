from django.contrib import admin
from baskets.admin import BasketTabAdmin
from orders.admin import OrderTabularAdmin
from users.models import User

# Register your models here.

#класс для отображения пользователей в админке
@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_display = ["username", "first_name", "last_name", "email"] # отображение полей 
    search_fields = ["username", "first_name", "last_name", "email"] # поля для поиска

    inlines = [BasketTabAdmin, OrderTabularAdmin] # позволяют отображать связанные модели внутри страницы пользователя 
    # BasketTabAdmin: Отображает корзины, связанные с пользователем
    # OrderTabularAdmin: Отображает заказы, связанные с пользователем 
