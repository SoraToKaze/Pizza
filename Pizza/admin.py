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

"""
@admin.register(Delivery)
@admin.register(Pizza)
"""