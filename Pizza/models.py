from django.db import models
from django.contrib.auth.models import User

class PizzaSizes(models.Model):
    size = models.CharField(max_length=20)

    def __str__(self):
        return self.size

class PizzaCrust(models.Model):
    crust = models.CharField(max_length=20)

    def __str__(self):
        return self.crust

class PizzaCheese(models.Model):
    cheese = models.CharField(max_length=20)

    def __str__(self):
        return self.cheese

class PizzaSauce(models.Model):
    sauce = models.CharField(max_length=20)

    def __str__(self):
        return self.sauce


######################## PIZZA MODEL
class Pizza(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    size = models.ForeignKey(PizzaSizes, on_delete=models.CASCADE)
    crust = models.ForeignKey(PizzaCrust, on_delete=models.CASCADE)
    sauce = models.CharField(PizzaSauce, on_delete=models.CASCADE)
    cheese = models.CharField(PizzaCheese, on_delete=models.CASCADE)
    toppings = models.ManyToManyField()
    
    # Automatically set the order date when the pizza is created.
    date = models.DateTimeField(auto_now_add=True, blank=True)

    def __str__(self):
        return f"Pizza by {self.author.username} on {self.date.strftime('%Y-%m-%d')}"

############# DELIVERY CONFIG

# Month choices for expiration date
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

# Year choices for expiration date
YEAR_CHOICES = tuple((year, year) for year in range(2025, 2050))

class Delivery(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    address = models.CharField(max_length=200)
    # For card numbers, consider using a CharField if you need to preserve leading zeros.
    cardNo = models.IntegerField()
    expMonth = models.CharField(max_length=15, choices=MONTH_CHOICES, default='January')
    expYear = models.IntegerField(choices=YEAR_CHOICES, default=2025)
    # IntegerField does not support max_length; if you need fixed-length, consider CharField.
    cvv = models.CharField(max_length=3)

    def __str__(self):
        return f"Delivery for {self.name} by {self.author.username}"