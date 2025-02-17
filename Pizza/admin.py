from django.contrib import admin
from .models import *

# Register your models here.
@admin.register(PizzaSizes)
class SizeAdmin(admin.ModelAdmin):
    list_display = ('size', )

@admin.register(PizzaCheese)
class CheeseAdmin(admin.ModelAdmin):
    list_display = ('cheese', )

@admin.register(PizzaSauce)
class SauceAdmin(admin.ModelAdmin):
    list_display = ('sauce', )

@admin.register(PizzaCrust)
class CrustAdmin(admin.ModelAdmin):
    list_display = ('crust', )

@admin.register(PizzaToppings)
class ToppingsAdmin(admin.ModelAdmin):
    list_display = ('top', )
    
@admin.register(Pizza)
class PizzaAdmin(admin.ModelAdmin):
    list_display = ('author', 'size', 'crust', 'sauce', 'cheese', 'top_list', 'date')
    def top_list(self, obj):
        return ", ".join([top.top for top in obj.toppings.all()])
    
@admin.register(Delivery)
class DeliveryAdmin(admin.ModelAdmin):
    list_display = ('author', 'name', 'address', 'cardNo', 'ExpiryMonth', 'ExpiryYear', 'cvv')
