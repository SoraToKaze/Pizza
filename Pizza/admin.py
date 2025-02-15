from django.contrib import admin
from .models import *

# Register your models here.
admin.register(PizzaSizes)
admin.register(PizzaCheese)
admin.register(PizzaSauce)
admin.register(PizzaCrust)
admin.register(PizzaToppings)
admin.register(Delivery)
admin.register(Pizza)

