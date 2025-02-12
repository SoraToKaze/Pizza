from django.db import models
from django.contrib.auth.models import User

class PizzaSizes(models.Model):
    size = models.CharField(max_length=20)

    def __str__(self):
        return self.size

class PizzaCrust(models.Model):
    crust = models.CharField(max_length=20)
    price = models.DecimalField(max_digits=6, decimal_places=2, default=0.00)

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

class PizzaToppings(models.Model):
    top = models.CharField(max_length=20)
    price = models.DecimalField(max_digits=6, decimal_places=2, default=0.50)

    def __str__(self):
        return self.top

class Pizza(models.Model):
    size = models.CharField(max_length=20, default ='Large')
    crust = models.CharField(max_length=20, default='Regular')
    sauce = models.CharField(max_length=20, default='Tomato')
    cheese = models.CharField(max_length=20, default='Mozzarella')
    toppings = models.ManyToManyField(PizzaToppings)
    
    date = models.DateTimeField(auto_now_add=True, blank=True)

    def __str__(self):
        return f"{self.size} pizza with {self.crust} crust, {self.sauce} sauce, {self.cheese} cheese, and{self.toppings}"

    @staticmethod
    def get_choices():
        pizzaSizes = tuple((size.size, size.size) for size in PizzaSizes.objects.all())
        pizzaCrustSize = tuple((item.crust, item.crust) for item in PizzaCrust.objects.all())
        pizzaSauce = tuple((item.sauce, item.sauce) for item in PizzaSauce.objects.all())
        pizzaCheese = tuple((item.cheese, item.cheese) for item in Cheese.objects.all())
        return pizzaSizes, pizzaCrustSize, pizzaSauce, pizzaCheese

    def save(self, *args, **kwargs):
        self.size = models.CharField(max_length=20, choices=self.get_choices()[0], default ='Large')
        self.crust = models.CharField(max_length=20, choices=self.get_choices()[1], default='Regular')
        self.sauce = models.CharField(max_length=20, choices=self.get_choices()[2], default='Tomato')
        self.cheese = models.CharField(max_length=20, choices=self.get_choices()[3], default='Mozzarella')
        super().save(*args, **kwargs)
    
class Order(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    pizzas = models.ManyToManyField(Pizza)  # Order can have multiple pizzas
    total_price = models.DecimalField(max_digits=6, decimal_places=2)
    order_date = models.DateTimeField(auto_now_add=True)
    delivery_address = models.TextField()

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

YEAR_CHOICES = tuple((year, year) for year in range(2025, 2050))

class Delivery(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    address = models.CharField(max_length=200)
    cardNo = models.IntegerField()
    expiryMonth = models.CharField(max_length=15, choices=MONTH_CHOICES, default='January')
    eYear = models.IntegerField(choices=YEAR_CHOICES, default=2025)
    cvv = models.IntegerField()

    def __str__(self):
        return f"Delivery for {self.name} by {self.author.username}"
    