from django.shortcuts import *
from django.contrib.auth import logout
from django.contrib.auth.models import User
from django.contrib.auth.views import LoginView
from django.contrib.auth import login, logout
from .forms import *
from django.contrib.auth.decorators import login_required
from django.contrib.auth import login

def index(request):
    return render(request, 'index.html')

def signup(request):
    if request.method == "POST":
        form = RegisterForm(request.POST)
        if form.is_valid():
            login(request, form.save())
            return redirect("order.html")
    else:
        form = RegisterForm()
    return render(request, "register.html", {"form":form})

class UserLoginForm(LoginView):
    template_name = "login.html"

def logout_view(request):
    logout(request)
    return redirect("/")
"""
@login_required(login_url='index.html')
def order_request(request):
    global delivering
    global pizza
    
    if request.method == "POST":
        form = PizzaForm(request.POST)
        if form.is_valid():
            pizza = form.save()=False
            pizza.author = request.user
            pizza.toppings = ', '.join(toppings)
"""