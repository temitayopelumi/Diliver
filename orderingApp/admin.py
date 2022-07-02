from django.contrib import admin
from .models import Table, Order, OrderItem, Menu
# Register your models here.

admin.site.register(Table)
admin.site.register(Order)
admin.site.register(OrderItem)
admin.site.register(Menu)
