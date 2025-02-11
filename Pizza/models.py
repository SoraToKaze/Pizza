from django.db import models
from django.contrib.auth.models import User

class PizzaToppings(models.Model):
    top = models.CharField(max_length=20)

    def __str__(self):
        return self.top

class PizzaSizes(models.Model):
    size = models.CharField(max_length=20)

    def __str__(self):
        return self.size

class PizzaCrust(models.Model):
    crust = models.CharField(max_length=20)

    def __str__(self):
        return self.crust

class PizzaSauce(models.Model):
    sauce = models.CharField(max_length=20)

    def __str__(self):
        return self.sauce

class Cheese(models.Model):
    cheese = models.CharField(max_length=20)

    def __str__(self):
        return self.cheese
######################## PIZZA MODEL
items = PizzaSizes.objects.all()
pizzaSizes = tuple((size.size, size.size) for size in items)

items = PizzaCrust.objects.all()
pizzaCrustSize = tuple((item.crust, item.crust) for item in items)

items = PizzaSauce.objects.all()
pizzaSauce = tuple((item.sauce, item.sauce) for item in items)

items = Cheese.objects.all()
pizzaCheese = tuple((item.cheese, item.cheese) for item in items)

class Pizza(models.Model):
    size = models.CharField(max_length=20, choices=pizzaSizes, default ='Large')
    crust = models.CharField(max_length=20, choices=pizzaCrustSize, default='Regular')
    sauce = models.CharField(max_length=20, choices=pizzaSauce, default='Tomato')
    cheese = models.CharField(max_length=20, choices=pizzaCheese, default='Mozzarella')
    toppings = models.ManyToManyField(PizzaToppings)
    
    date = models.DateTimeField(auto_now_add=True, blank=True)

    def __str__(self):
        return f"{self.size} pizza with {self.crust} crust, {self.sauce} sauce, {self.cheese} cheese, and{self.toppings}"
    
MONTH_CHOICES = (
    ("January", "January"),
    ("February", "February"),
    ("March", "March"),
    ("April", "April"),
    ("May", "May"),
    ("June", "June"),
    ("July", "July"),
    ("August", "August"),
    ("September", "September"),
    ("October", "October"),
    ("November", "November"),
    ("December", "December"),
)

YEAR_CHOICES = tuple((year, year) for year in range(2022, 2050))

class Delivery(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    address = models.CharField(max_length=200)
    cardNo = models.IntegerField()
    Month = models.CharField(max_length=15, choices=MONTH_CHOICES, default='January')
    eYear = models.IntegerField(choices=YEAR_CHOICES, default=2025)
    cvv = models.IntegerField()

    def __str__(self):
        return f"Delivery for {self.name} by {self.author.username}"