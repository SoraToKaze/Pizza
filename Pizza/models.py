from django.db import models
from django.contrib.auth.models import User

class PizzaToppings(models.Model):
    topping = models.CharField(max_length=20)

    def __str__(self):
        return self.topping

class Sizes(models.Model):
    size = models.CharField(max_length=20)

    def __str__(self):
        return self.size

class Crust(models.Model):
    crust = models.CharField(max_length=20)

    def __str__(self):
        return self.crust

class Cheese(models.Model):
    cheese = models.CharField(max_length=20)

    def __str__(self):
        return self.cheese

class Sauce(models.Model):
    sauce = models.CharField(max_length=20)

    def __str__(self):
        return self.sauce


######################## PIZZA MODEL
class Pizza(models.Model):
    # All customisation options will be done through the admin panel
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    size = models.ForeignKey(Sizes, on_delete=models.CASCADE)
    crust = models.ForeignKey(Crust, on_delete=models.CASCADE)
    sauce = models.CharField(Sauce, on_delete=models.CASCADE)
    cheese = models.CharField(Cheese, on_delete=models.CASCADE)
    toppings = models.ManyToManyField(PizzaToppings, through='PizzaToppingsChoices')
    
    # Automatically set the date to the current date and time when the object is created.
    date = models.DateTimeField(auto_now_add=True, blank=True)

    def __str__(self):
        return f"Pizza by {self.author.username} on {self.date.strftime('%Y-%m-%d')}"
    
    
class PizzaToppingsChoices(models.Model):
    pizza = models.ForeignKey(Pizza, on_delete=models.CASCADE)
    topping = models.ForeignKey(PizzaToppings, on_delete=models.CASCADE, related_name='topping')

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
    cardNo = models.IntegerField()
    expMonth = models.CharField(max_length=15, choices=MONTH_CHOICES, default='January')
    expYear = models.IntegerField(choices=YEAR_CHOICES, default=2025)
    cvv = models.CharField(max_length=4)

    def __str__(self):
        return f"Delivery for {self.name} by {self.author.username}"