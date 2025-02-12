from django import forms
from .models import *
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User

class SignUpForm(UserCreationForm):
    firstname = forms.CharField(max_length=50, required=True)
    lastname = forms.CharField(max_length=50, required=True)
    email = forms.EmailField(required=True)
    
    password1 = forms.CharField(
        label="Password",
        strip=False,
        widget=forms.PasswordInput,
        )
    
    password2 = forms.CharField(
        label="Password",
        strip=False,
        widget=forms.PasswordInput,
        )
    class Meta:
        model = User
        fields = ["firstname", "lastname", "username", "email", "password1", "password2"]
    def save(self, commit=True):
        user = super(SignUpForm, self).save(commit=False)
        user.email = self.cleaned_data["email"]
        if commit:
            user.save()
        return user

class LoginForm(AuthenticationForm):
    pass
        
class PizzaForm(forms.ModelForm):
    class Meta:
        model = Pizza
        fields = ['size', 'crust', 'sauce', 'cheese', 'toppings']
        widgets = {
            'toppings': forms.CheckboxSelectMultiple(),
        }

class DeliveryForm(forms.Form):
    class Meta:
        model = Delivery
        fields = ['author', 'name', 'address', 'cardNo', 'expiryMonth', 'expYear', 'cvv']