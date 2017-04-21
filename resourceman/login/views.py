from django.contrib.auth.models import User
from django.core.checks import messages

from .forms import LoginForm

__author__ = 'matt'

from django.contrib.auth import authenticate, login
from django.shortcuts import redirect, render_to_response, render
import logging

logger = logging.getLogger(__name__)

def login_view(request):
    """
    Pagina de login
    :param request: 
    :return: 
    """
    mensaje = ''
    if request.method == "POST":
        form = LoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['Usuario']
            password = form.cleaned_data['Clave']
            usuario = authenticate(username=username, password=password)
            if usuario is not None and usuario.is_active:
                login(request, usuario)
                logger.info('Login de Usuario %s' % request.user.username)
                return redirect('login/login.html')
            else:
                mensaje = 'Disculpa, el Nombre de Usuario o la Clave no coinciden.'
    formulario = LoginForm()
    return render(request, 'login/login.html', {"formulario": formulario})

