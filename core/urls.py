from distutils import core
from django import urls
from django.urls import path
from .views import *
from django.urls import path, include

urlpatterns = [
    path('', index, name='index'),
    path('login_ingresar',login_ingresar,name='login_ingresar')
    
] 


