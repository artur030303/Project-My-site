from django.contrib import admin
from baskets.admin import BasketTabAdmin
from users.models import User

# Register your models here.


@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_display = ["username", "first_name", "last_name", "email"]
    search_fields = ["username", "first_name", "last_name", "email"]

    inlines = [
        BasketTabAdmin,
    ]
