from django.contrib import admin
from .models import *


class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name', 'parent')

class CartAdmin(admin.ModelAdmin):
    list_display = ('product', 'cart')

class OrderAdmin(admin.ModelAdmin):
    list_display = ('user', 'id', 'total_cost', 'created_at','status', 'updated_at')

class ProductOrderAdmin(admin.ModelAdmin):
    list_display = ('product', 'order', 'quantity')

# Register your models here.
admin.site.register(UserProfile)
admin.site.register(Category, CategoryAdmin)
admin.site.register(Product)
admin.site.register(Cart)
admin.site.register(CartItem,CartAdmin)
admin.site.register(Order, OrderAdmin)
admin.site.register(ProductOrder, ProductOrderAdmin)