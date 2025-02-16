from . import views
from django.urls import path
from .forms import *

urlpatterns = [
    path('', views.index, name='index'),
    path('', views.logout_view, name='logout'),
    path('login/', views.login_view, name='login'),
    path('register/', views.register, name='register'),
    path('history_orders/', views.history_orders, name='history_orders'),
    path('create/', views.create, name='create'),
    path('confirmation/', views.confirmation, name='confirmation'),
    path('delivery/', views.delivery, name='delivery'),
    
]