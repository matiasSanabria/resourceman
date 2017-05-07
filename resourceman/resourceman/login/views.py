from django.contrib import auth

from .forms import LoginForm
from django.contrib.auth import authenticate, login, logout
from django.shortcuts import redirect, render
import logging

__author__ = 'matt'


def login_view(request):
    """
    Pagina de login
    :param request: 
    :return: muestra la vista de login del sistema
    """
    message = None
    if request.method == "POST":
        formulario = LoginForm(request.POST)
        if formulario.is_valid():
            username = request.POST['username']
            password = request.POST['password']
            usuario = authenticate(username=username, password=password)
            if usuario is not None:
                if usuario.is_active:
                    login(request, usuario)
                    message = "Ingreso correcto"
                    return redirect('index')
                else:
                    # si el usuario no esta activo
                    message = "El usuario esta inactivo"
            else:
                # si el usuario no existe
                message = "Nombre de usuario y/o contrasenha incorrecto"
    else:
        formulario = LoginForm()
    return render(request, 'login/login.html', {"message": message, "formulario": formulario})


def logout_view(request):
    """
        Cierra la sesión del usuario y retorna a la vista de login.
    """
    auth.logout(request)
    return redirect('login')

