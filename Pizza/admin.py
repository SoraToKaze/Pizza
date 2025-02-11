from django.contrib import admin
from .models import *

# Register your models here.
admin.register(PizzaSizes)
admin.register(PizzaCrust)
admin.register(Cheese)
admin.register(PizzaSauce)
admin.register(PizzaToppings)
admin.register(Delivery)