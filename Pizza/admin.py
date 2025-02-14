from django.contrib import admin
from .models import *

# Register your models here.
@admin.register(PizzaSizes)
class SizeAdmin(admin.ModelAdmin):
    list_display = ('name', )
    
@admin.register(PizzaCheese)
class CheeseAdmin(admin.ModelAdmin):
    list_display = ('name', )

@admin.register(PizzaSauce)
class SauceAdmin(admin.ModelAdmin):
    list_display = ('name', )
    
@admin.register(PizzaCrust)
class CrustAdmin(admin.ModelAdmin):
    list_display = ('name', )

@admin.register(PizzaToppings)
class ToppingsAdmin(admin.ModelAdmin):
    list_display = ('name', )

@admin.register(Delivery)
class SizeAdmin(admin.ModelAdmin):
    list_display = ('name', )

@admin.register(Pizza)
class PizzaAdmin(admin.ModelAdmin):
    list_display = ('size', 'sauce', 'crust', 'cheese', 'toppings_on_pizza', 'user', 'created_at')
    
    def toppings_on_pizza(self, obj):
        return ", ".join((topping.name for topping in obj.toppings.all()))
    toppings_on_pizza.short_description = 'Toppings'

@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    list_display = ('user', 'pizza', 'delivery_details', 'create_time')