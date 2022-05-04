

from django.shortcuts import render
from core.forms import LoginForm
from .forms import *
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required


from django.http import JsonResponse

# Create your views here.
def index(request):
    return render(request, 'core/index.html', {})

def login_ingresar(request):
    message = None
    if request.method == "POST":
        form = LoginForm(request.POST)
        if form.is_valid():
            username = request.POST['username']
            password = request.POST['password']
            user = authenticate(username=username, password=password)
            if user is not None:
                if user.is_active:
                    login(request, user)
                    message = "Te has identificado de modo correcto"
                    return render(request,'core/django_administrador.html', {'message': message, 'form':form})
                    #return render(request,'core/index.html', {'message': message, 'form':form})
                else:
                    message = "Tu usuario esta inactivo"
            else:
                message = "nombre de usuario y/o password incorrecto"
    else:
        form = LoginForm()
    return render(request,'core/login_ingresar.html', {'message': message, 'form':form})
























