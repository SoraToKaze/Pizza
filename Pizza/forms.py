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
        fields = ['size', 'crust', 'sauce', 'cheese', 'toppings']
        widgets = {
            'toppings': forms.CheckboxSelectMultiple,
        }

class DeliveryForm(forms.ModelForm):
    class Meta:
        model = Delivery
        fields = ["name","address", "cardNo", "Month", "Year", "cvv"]
        
"""""
class OrderForm(forms.ModelForm):
    class Meta:
        model = Order
        fields = ['pizza', 'toppings', 'customer_name', 'customer_address', 'customer_phone']
        widgets = {
            'pizza': forms.Select(attrs={'class': 'form-control'}),
            'toppings': forms.CheckboxSelectMultiple(attrs={'class': 'form-check-input'}),
            'customer_name': forms.TextInput(attrs={'class': 'form-control'}),
            'customer_address': forms.Textarea(attrs={'class': 'form-control'}),
            'customer_phone': forms.TextInput(attrs={'class': 'form-control'}),
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # Customize the pizza field to include crust, size, and sauce
        self.fields['pizza'].label_from_instance = lambda obj: f"{obj.name} ({obj.size}, {obj.crust}, {obj.sauce})"

"""