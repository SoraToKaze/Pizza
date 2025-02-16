from django.db import models
from django.contrib.auth.models import User
from django.core.validators import MinLengthValidator, MaxLengthValidator, RegexValidator

class PizzaSizes(models.Model):
    size = models.CharField(max_length=20)

class PizzaSauce(models.Model):
    sauce = models.CharField(max_length=20)

class PizzaCheese(models.Model):
    cheese = models.CharField(max_length=20)

class PizzaToppings(models.Model):
    top = models.CharField(max_length=30)

class PizzaCrust(models.Model):
    crust = models.CharField(max_length=20)

class Pizza(models.Model):

    author =   models.ForeignKey(User, on_delete=models.CASCADE)
    size =     models.ForeignKey(PizzaSizes, on_delete=models.CASCADE)
    crust =    models.ForeignKey(PizzaCrust, on_delete=models.CASCADE)
    sauce =    models.ForeignKey(PizzaSauce, on_delete=models.CASCADE)
    cheese =  models.ForeignKey(PizzaCheese, on_delete=models.CASCADE)
    toppings = models.ManyToManyField(PizzaToppings)
    date =     models.DateTimeField(auto_now_add=True, blank=True)

    def __str__(self):
        
        return f"{self.size} pizza with {self.crust} crust, {self.sauce} sauce, {self.cheese} cheese, and{self.toppings} at {self.date.strftime('%Y-%m-%d')}"
MONTH_CHOICES = tuple((month, month) for month in range(1, 12))
YEAR_CHOICES = tuple((year, year) for year in range(2025, 2050))

class Delivery(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    pizza = models.OneToOneField('Pizza', on_delete=models.CASCADE, null=True)
    name = models.CharField(max_length=100)
    address = models.CharField(max_length=200)
    cardNo = models.CharField(max_length=16, 
        validators=[
            MinLengthValidator(16), 
            MaxLengthValidator(16), 
            RegexValidator(r'^\d{16}$', 'Enter a valid 16-digit card number')
            ],
        help_text="Enter 16 digit card number. No spaces!"
    )
    expiryMonth = models.IntegerField(choices=MONTH_CHOICES, default=1)
    eYear = models.IntegerField(choices=YEAR_CHOICES, default=2025)
    cvv = models.CharField(
        max_length=3,
        validators=[
            MinLengthValidator(3),
            MaxLengthValidator(3),
            RegexValidator(r'^\d{3}$', 'Enter a valid 3-digit CVV')
        ],
        help_text="Enter the 3 digit CVV at the back of your card"
    )
    def __str__(self):
        return f"Delivery for {self.name} by {self.author.username}"


class Confirm_Order(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    pizza = models.ForeignKey(Pizza, on_delete=models.CASCADE)
    delivery = models.ForeignKey(Delivery, on_delete=models.CASCADE)
    create_time = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return f"Order #{self.id} by {self.user.username}"
    
