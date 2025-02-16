from django import forms
from .models import *
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User

class RegisterForm(UserCreationForm):
    class Meta:
        model = User
        fields = ["username", "email", "password1", "password2"]

    def save(self, commit=True):
        user = super(RegisterForm, self).save(commit=False)
        user.email = self.cleaned_data["email"]
        if commit:
            user.save()
        return user
class LoginForm(AuthenticationForm):
    def __init__(self, *args, **kwargs):
        super(LoginForm, self).__init__(*args, **kwargs)
        self.fields['username'].widget.attrs.update({'class': 'form-control', 'placeholder': 'Username'})
        self.fields['password'].widget.attrs.update({'class': 'form-control', 'placeholder': 'Password'})
        
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

        widgets = {
            'card_number': forms.NumberInput(attrs={
                'placeholder': 'XXXX-XXXX-XXXX-XXXX',
                'minlength': 16,
                'maxlength': 16,
            }),

            'expiryMonth': forms.NumberInput(attrs={
                'placeholder': 'MM',
                'min': 1,
                'max': 12,
            }),

            'expYear': forms.NumberInput(attrs={
                'placeholder': 'YY',
                'min': 0,
                'max': 99,
            }),
            
            'cvv': forms.TextInput(attrs={
                'placeholder': 'CVV',
                'min': 0,
                'max': 999,
            }),
        }
