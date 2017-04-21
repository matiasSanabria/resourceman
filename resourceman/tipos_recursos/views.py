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


def editar(request, nombre):
    mensaje = 'Modificar Permiso'
    messages.add_message(request, messages.INFO, mensaje)
    editar = TipoRecurso.objects.get(nombre=nombre)

    if request.method == 'POST':
        editar_form = TipoRecursoForm(request.POST, instance=editar)
        if editar_form.is_valid():
            editar_form.save()
            return redirect('listar')
        else:
            editar_form = TipoRecursoForm(request.POST, instance=editar)

        return render(request, 'tipo_recurso/editar_tipo_recurso.html', {
            'editar_form': editar_form,
            'nombre': nombre
        })
    else:
        editar_form = TipoRecursoForm(instance=editar)
        return render(request, 'tipo_recurso/editar_tipo_recurso.html', {
            'editar_form': editar_form,
            'nombre': nombre
        })


@login_required
def eliminar(request, nombre):
    eliminar = TipoRecurso.objects.get(nombre=nombre)
    mensaje = "Tipo de Recurso \'%s\' eliminado..\n" % eliminar
    messages.add_message(request, messages.INFO, mensaje)
    eliminar.delete()
    return redirect('../listar')


@login_required
def listar_tipos_recursos(request):
    mensaje = 'Listar Permisos'
    messages.add_message(request, messages.INFO, mensaje)
    lista = TipoRecurso.objects.filter(estado='A')
    return render(request, 'tipo_recurso/listar_tipos_recursos.html', {'lista': lista})
