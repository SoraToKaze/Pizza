from django.contrib import admin
from .models import *

# Register your models here.
admin.register(Sizes)
admin.register(Crust)
admin.register(Cheese)
admin.register(Sauce)
admin.register(Pizza)
admin.register(Delivery)