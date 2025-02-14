from django import forms
from .models import *
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from crispy_forms.layout import Layout, Submit
from crispy_forms.helper import FormHelper

class RegisterForm(UserCreationForm):
    class Meta:
        model = User
        fields = ["username", "email", "first_name", "last_name", "password1", "password2"]

    def save(self, commit=True):
        user = super(RegisterForm, self).save(commit=False)
        user.email = self.cleaned_data["email"]
        user.first_name = self.cleaned_data["first_name"]
        user.last_name = self.cleaned_data["last_name"]
        if commit:
            user.save()
        return user
class PizzaForm(forms.ModelForm):
    class Meta:
        model = Pizza
        fields = ['size', 'crust', 'sauce', 'cheese', 'toppings']
        widgets = {
            'toppings' : forms.CheckboxSelectMultiple(), #allows user to pick more than one topping at a time
        }
        
class DeliveryForm(forms.Form):
    class Meta:
        model = Delivery
        fields = ['name', 'address', 'cardNo', 'expiryMonth', 'expYear', 'cvv']
