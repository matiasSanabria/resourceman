from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.models import User
from django.core.checks import messages
from django.template import RequestContext

from .forms import LoginForm

__author__ = 'matt'

from django.contrib.auth import authenticate, login, logout
from django.shortcuts import redirect, render_to_response, render
import logging

logger = logging.getLogger(__name__)


def login_view(request):
    """
    Pagina de login
    :param request: 
    :return: muestra la vista de login del sistema
    """
    if not request.user.is_anonymous():
        return redirect('index.html')
    if request.method == "POST":
        formulario = LoginForm(request.POST)
        if formulario.is_valid():
            username = request.POST['username']
            password = request.POST['password']
            usuario = authenticate(username=username, password=password)
            if usuario is not None:
                if usuario.is_active:
                    login(request, usuario)
                    return redirect('index.html')
                else:
                    # si el usuario no esta activo
                    return render_to_response('login/login.html', context_instance=RequestContext(request))
            else:
                # si el usuario no existe
                return render_to_response('login/login.html', context_instance=RequestContext(request))
    else:
        formulario = LoginForm()
    return render(request, 'login/login.html', {"formulario": formulario})


def logout_view(request):
    """
        Cierra la sesión del usuario y retorna a la vista de login.
    """
    logout(request)
    return redirect('/login')
