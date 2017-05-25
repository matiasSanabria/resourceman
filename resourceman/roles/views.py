from django.contrib.auth.decorators import login_required

__author__ = 'hector'

from .forms import EditarRol, AgregarRol
from django.contrib.auth.models import Group
from django.contrib import messages
from django.shortcuts import render, redirect


@login_required
def agregarRol(request):
    """
    Página para la agregacion de Rol.

    Recibe los datos suministrados por el usuario a traves de un post.

    Se define un objeto para guardar los datos a traves de la funcion del form.

    """
    mensaje = 'Crear Rol'
    messages.add_message(request, messages.INFO, mensaje)

    if request.method == 'POST':

        if AgregarRol(request.POST).is_valid():
            rol_form = AgregarRol(request.POST)
            rol_form.save(commit=True)
            return redirect('agregarRol')# direccion url de la app
        else:
            mensaje = "Error, intente datos diferentes"
            messages.add_message(request, messages.INFO, mensaje)
            rol_form = AgregarRol()  # crea una instancia permiso_form vacia con el constructor PermisoForm()
    else:
        rol_form = AgregarRol()
        return render(request, 'roles/agregarRoles.html', {
            'rol_form': rol_form,
        })


@login_required
def listarRol(request):
    """
    Página para listar de rol.

    Genera una instancia de los objetos de Group y luego los devuleve al template listarRoles.html

    """
    mensaje = 'Listar Rol'
    messages.add_message(request, messages.INFO, mensaje)
    roles = Group.objects.all()
    return render(request, 'roles/listarRoles.html', {
        'roles': roles
    })


@login_required
def eliminarRol(request, pk):
    """
    Página para la eliminacion de rol.

    Recibe un Post con un atributo pk del rol a eliminar.

    Se instancia el objeto con el identificador suministrado.

    Se procede a eliminar el objeto con el metodo delete().

    """
    eliminar = Group.objects.get(pk=pk)
    mensaje = "Roles \'%s\' eliminado..\n" % eliminar
    messages.add_message(request, messages.INFO, mensaje)
    eliminar.delete()
    return redirect('../listar')


@login_required
def editarRol(request, pk):
    """
    Página para la edicion de rol.

    Recibe un Post con un atributo pk del rol a editar.

    Se instancia el objeto con el identificador suministrado.

    Se alteran los datos con el Post recibido y se guardan.
    """
    mensaje = 'Modificar Permiso'
    messages.add_message(request, messages.INFO, mensaje)
    editar = Group.objects.get(id=pk)

    if request.method == 'POST':
        editar_form = EditarRol(request.POST, instance=editar)
        if editar_form.is_valid():
            editar_form.save()
            return redirect('listarRol')
        else:
            editar_form = EditarRol(request.POST, instance=editar)

        return render(request, 'roles/editarRoles.html', {
            'editar_form': editar_form,
            'pk': pk
        })
    else:
        editar_form = EditarRol(instance=editar)
        return render(request, 'roles/editarRoles.html', {
            'editar_form': editar_form,
            'pk': pk
        })