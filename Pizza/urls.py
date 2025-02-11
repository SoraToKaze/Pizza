from . import views
from django.urls import path
from .forms import *

urlpatterns = [
    path('', views.index, name='index'),
    path('logout/', views.logout_view, name='logout'),
    path('login', views.login_view, name='login'),
    path('signup', views.register_view, name='register'),
]