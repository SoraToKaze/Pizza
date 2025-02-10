from django.shortcuts import *
from django.contrib.auth import logout
from .forms import RegisterForm
from django.http import HttpResponseRedirect
from django.contrib.auth.models import User
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.contrib.auth import login, logout
from .forms import LoginForm, RegisterForm

def index(request):
    return render(request, 'index.html')
def login(request):
    return render(request, 'login.html')

def register_view(request):
    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            login(request, form.save())
            return redirect("index.html")
    else:
        form = UserCreationForm()
    return render(request, "register.html", {"form":form})


def login_view(request):
    if request.method == "POST":
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect("index.html")
    else:
        form = AuthenticationForm()
    return render(request, "login.html", {"form":form})

def logout_view(request):
    if request.method == "POST":
        logout(request)
        return HttpResponseRedirect('index.html')