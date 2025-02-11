from django import forms
from .models import *
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User

class RegisterForm(UserCreationForm):
    firstname = forms.CharField(max_length=50)
    lastname = forms.CharField(max_length=50)
    email = forms.EmailField()
    
    password1 = forms.CharField(
        label="Password",
        strip=False,
        widget=forms.PasswordInput,
        )
    
    password2 = forms.CharField( label="Password",
        strip=False,
        widget=forms.PasswordInput,
        )
    class Meta:
        model = User
        fields = ["firstname", "lastname", "username", "email", "password1", "password2"]
    def save(self, commit=True):
        user = super(RegisterForm, self).save(commit=False)
        user.email = self.cleaned_data["email"]
        if commit:
            user.save()
        return user

class LoginForm(AuthenticationForm):
    username = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control'}))
    password = forms.CharField(widget=forms.PasswordInput(attrs={'class': 'form-control'}))
        
class PizzaForm(forms.ModelForm):
    class Meta:
        model = Pizza
        fields = ["size", "crust", "sauce", "cheese", "toppings"]

class DeliveryForm(forms.ModelForm):
    class Meta:
        model = Delivery
        fields = ["name","address", "card_number", "Exp_month", "Exp_year", "CVV"]
