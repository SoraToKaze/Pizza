from django.contrib import admin
from .models import *

# Register your models here.
admin.register(PizzaSizes)
admin.register(PizzaCrust)
admin.register(Cheese)
admin.register(PizzaSauce)
admin.register(PizzaToppings)
admin.register(Delivery)

@admin.register(Pizza)
class PizzaAdmin(admin.ModelAdmin):
    list_display = ["size", "crust", "sauce", "cheese"]
    filter_horizontal = ("toppings",)  

"""
@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    list_display = ["user", "total_price", "order_date"]
"""