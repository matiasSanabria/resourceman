from django.contrib.auth.decorators import login_required
from django.shortcuts import render_to_response, redirect, render
from .forms import TipoRecursoForm
from .models import TipoRecurso
from django.contrib import messages

__author__ = 'matt'

@login_required
def crear(request):
    if request.method == "POST":
        tipo_recurso = TipoRecursoForm(request.POST)
        if tipo_recurso.is_valid():
            tipo_recurso.save()
            return redirect('tipo_recurso/crear')
        else:
            pass
    tipo_recurso = TipoRecursoForm()
    return render(request, 'tipo_recurso/crear_tipos_recursos.html', {'tipo_recurso': tipo_recurso})

@login_required
def listar_tipos_recursos(request):
    mensaje = 'Listar Permisos'
    messages.add_message(request, messages.INFO, mensaje)
    lista_tr = TipoRecurso.objects.filter(estado='A')
    return render(request, "tipo_recurso/listar_tipos_recursos.html", {'lista_tr': lista_tr})
