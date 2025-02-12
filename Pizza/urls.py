from . import views
from django.urls import path
from .forms import *

urlpatterns = [
    path('', views.index, name='index'),
    path('', views.logout_view, name='logout'),
    path('login/', views.UserLoginForm.as_view, name='login'),
    path('register/', views.signup, name='register'),
]