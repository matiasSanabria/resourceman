__author__ = 'hector'

from django.shortcuts import render, redirect, render_to_response

from django.contrib import messages
from .forms import *



from django.shortcuts import render_to_response
from .forms import EditarPermisos, AgregarPermiso
from django.contrib.auth.models import Group, Permission



def listarPermisos(request):
    """
        Página para listar de permiso.

        Genera una instancia de los objetos de Permission y luego los devuleve al template listarPermiso.html

    """
    mensaje = 'Listar Permisos'
    messages.add_message(request, messages.INFO, mensaje)
    aux = Permission.objects.all().order_by('id')
    permisos = aux[21:]
    return render(request, 'permisos/listarPermisos.html', {
        'permisos': permisos
    })


def editarPermiso(request, pk):
    """
        Página para la edicion de permiso.

        Recibe un Post con un atributo pk del permiso a editar.

        Se instancia el objeto con el identificador suministrado.

        Se alteran los datos con el Post recibido y se guardan.

    """
    mensaje = 'Modificar Permiso'
    messages.add_message(request, messages.INFO, mensaje)
    # mod = Permission.objects.get(pk=pk)
    editar= Permission.objects.get(id=pk)
    # editar_form= EditarPermisos(instance=editar)

    if request.method == 'POST':
        editar_form = EditarPermisos(request.POST, instance=editar)
        if editar_form.is_valid():
            editar_form.save()
            return redirect('listarPermisos')
        else:
            editar_form = EditarPermisos(request.POST, instance=editar)

        return render(request, 'permisos/editarPermisos.html', {
            'editar_form': editar_form,
            'pk': pk
        })
    else:
        editar_form = EditarPermisos(instance=editar)
        return render(request, 'permisos/editarPermisos.html', {
            'editar_form': editar_form,
            'pk': pk
        })

def eliminarPermiso(request, pk):
    """
            Página para la eliminacion de permiso.

            Recibe un Post con un atributo pk del permiso a eliminar.

            Se instancia el objeto con el identificador suministrado.

            Se procede a eliminar el objeto con el metodo delete().

    """
    eliminar = Permission.objects.get(pk=pk)
    mensaje = "Permiso \'%s\' eliminado..\n" % eliminar
    messages.add_message(request, messages.INFO, mensaje)
    eliminar.delete()
    return redirect('../listar')

def agregarPermiso(request):
    """
        Página para la agregacion de permiso.

        Recibe los datos suministrados por el usuario a traves de un post.

        Se define un objeto para guardar los datos a traves de la funcion del form.

    """

    mensaje = 'Crear Permiso'
    messages.add_message(request, messages.INFO, mensaje)

    if request.method == 'POST':
        name = request.POST.get("name")
        codename = request.POST.get("codename")
        content_type = request.POST.get("content_type")

        if AgregarPermiso(request.POST).is_valid():
            print("si es valido")
            permiso_form = AgregarPermiso(request.POST)
            permiso_form.save(commit=True)
            mensaje = "Permiso \'%s\' creado..\n" % name
            messages.add_message(request, messages.INFO, mensaje)
            return redirect('agregar')# direccion url de la app
        else:
            print("no es valido")
            mensaje = "Error, intente datos diferentes"
            messages.add_message(request, messages.INFO, mensaje)
            permiso_form = AgregarPermiso()  # crea una instancia permiso_form vacia con el constructor PermisoForm()
    else:
        permiso_form = AgregarPermiso()
        return render(request, 'permisos/agregarPermisos.html', {
            'permiso_form': permiso_form,
        })