from django.contrib import admin
from .models import *

# Register your models here.
admin.register(PizzaSizes)
admin.register(PizzaCrust)
admin.register(PizzaCheese)
admin.register(PizzaSauce)
admin.register(Pizza)
admin.register(Delivery)