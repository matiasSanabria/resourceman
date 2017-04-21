from django.views.decorators.csrf import csrf_exempt

__author__ = 'matt'

from django.contrib.auth import authenticate, login
from django.contrib.auth.models import Permission
from django.shortcuts import render_to_response
from django.http import HttpResponseRedirect
from django.template import RequestContext
from .forms import LoginForm
import logging

logger = logging.getLogger(__name__)

def login(request):
    message = ''
    if request.method == "POST":
        form = LoginForm(request.POST)

        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = authenticate(username=username, password=password)

            if user is not None and user.is_active:
                login(request, user)
                logger.info("Login de usuario %s" % request.user.username)
                return HttpResponseRedirect("/")
            else:
                message = "El nombre de usuario o password no coinciden"

    formulario = LoginForm()
    #ctx = {'formulario': formulario, 'mensaje': message}
    return render_to_response('login/login.html', {'formulario': formulario}, RequestContext(request))
