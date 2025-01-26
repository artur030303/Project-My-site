from django.contrib import admin

from orders.models import Order, OrderItem



# класс для отображения товаров в заказе, в админке, в виде таблице
class OrderItemTabulareAdmin(admin.TabularInline):
    model = OrderItem # класс модели
    fields = "product", "name", "price", "quantity"# поля модели
    search_fields = ("product","name",)# поля поиска
    extra = 0 # устанавливает количество дополнительных пустых строк для добавления новых объектов на 0 (по умолчанию их 3)


# 
@admin.register(OrderItem)# регистрация модели
class OrderItemAdmin(admin.ModelAdmin):
    list_display = "order", "product", "price", "quantity" # поля, которые будут отображаться в таблице списка объектов
    search_fields = ("order","product","name",) # поля поиска 

 #  класс предназначен для отображения связанных объектов Order в виде табличного интерфейса
class OrderTabularAdmin(admin.TabularInline):
    model = Order 
    fields = ("status","user","phone_number","created_timestamp",)# отображение полей модели
    readonly_fields = ("created_timestamp",)# отображение только для чтения
    extra = 0 # устанавливает количество дополнительных пустых строк для добавления новых объектов на 0 (по умолчанию их 3)


# 
@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    list_display = "user", "phone_number", "status", "created_timestamp"# поля, которые будут отображаться в таблице списка объектов
    search_fields = ("id",)# поле поиска по id
    readonly_fields = ("created_timestamp",)# отображение только для чтения
    list_filter = ("status",)#  возможность фильтровать заказы по статусу
    inlines = (OrderItemTabulareAdmin,)# Связывает админ OrderAdmin с OrderItemTabulareAdmin, чтобы в карточке заказа отображались связанные товары
