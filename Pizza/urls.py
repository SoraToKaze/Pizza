from . import views
from django.urls import path
from .forms import *
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('', views.index, name='index'),
    path('', views.logout_view, name='logout'),
    path('login/', views.login, name='login'),
    path('register/', views.signup, name='register'),
    path('history_orders/', views.history_orders, name='history_orders'),
    path('create/', views.create, name='create'),
    path('confirmation/', views.confirmation, name='confirmation'),
    path('delivery/', views.delivery, name='delivery'),
    
]