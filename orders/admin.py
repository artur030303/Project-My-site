from django.contrib import admin

from orders.models import Order, OrderItem

# Register your models here.


class OrderItemTabulareAdmin(admin.TabularInline):
    model = OrderItem
    fields = "product", "name", "price", "quantity"
    search_fields = (
        "product",
        "name",
    )
    extra = 0


@admin.register(OrderItem)
class OrderItemAdmin(admin.ModelAdmin):
    list_display = "order", "product", "price", "quantity"
    search_fields = (
        "order",
        "product",
        "name",
    )


class OrderTabularAdmin(admin.TabularInline):
    model = Order
    fields = (
        "status",
        "user",
        "phone_number",
        "created_timestamp",
    )
    readonly_fields = ("created_timestamp",)
    extra = 0


@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    list_display = "user", "phone_number", "status", "created_timestamp"
    search_fields = ("id",)
    readonly_fields = ("created_timestamp",)
    list_filter = ("status",)
    inlines = (OrderItemTabulareAdmin,)
