from . import views
from django.urls import path
from .forms import *
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('', views.index, name='index'),
    path('', views.logout_view, name='logout'),
    path('login/', auth_views.UserLoginForm.as_view, name='login'),
    path('register/', views.signup, name='register'),
]