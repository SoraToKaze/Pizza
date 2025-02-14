from django.shortcuts               import render, redirect
from django.contrib.auth.views      import LoginView
from django.contrib.auth            import logout, login, authenticate
from django.contrib.auth.decorators import login_required
from django.contrib                 import messages
from .models                        import *
from .forms                         import *

def index(request):
    return render(request, 'index.html')

def register(request):
    if request.method == "POST":
        form = RegisterForm(request.POST)
        
        if form.is_valid():
            form.save()
            return redirect("/")
    else:
        form = RegisterForm()
    return render(request, "register.html", {"form":form})

class UserLoginView(LoginView):
    pass

def login(request):
    if request.method == "POST":
        form = UserLoginView(request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('/index')
    else:
        form = UserLoginView()
    return render(request, "login.html", {"form":form})

def logout_view(request):
    logout(request)
    return redirect("/")

@login_required(login_url='index')
def history_orders(request):
    orders = Delivery.objects.filter(author=request.user).select_related('pizza')
    return render(request, "history_orders.html", {'orders': orders})

@login_required(login_url='index')
def create(request):

    if request.method == "POST":
        form = PizzaForm(request.POST)
        
        if form.is_valid():
            pizza = form.save(commit=False) #Makes a new pizza without it going to the database
            pizza.author = request.user
            pizza.save()
            form.save_m2m()
            return redirect('/delivery')
    else:
        form = PizzaForm()
    return render(request, "/create.html", {'form':form})

@login_required(login_url='index')
def confirmation(request):
    pizza_id = request.session.get('pending_pizza_id')
    if not pizza_id:
        messages.error(request, 'You must create a pizza first') 
        return redirect('/create')
    if request.method == 'POST':
        form = DeliveryForm(request.POST)
        if form.is_valid():
            delivery = form.save(commit=False)
            delivery.author = request.user