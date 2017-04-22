
from .forms import EditarRol, AgregarRol
from django.contrib.auth.models import Group, Permission
from django.contrib import messages
from django.shortcuts import render, redirect, render_to_response

# Create your views here.
def agregarRol(request):
    mensaje = 'Crear Rol'
    messages.add_message(request, messages.INFO, mensaje)

    if request.method == 'POST':
        # name = request.POST.get("name")
        # codename = request.POST.get("codename")
        # content_type = request.POST.get("content_type")

        if AgregarRol(request.POST).is_valid():
            print("si es valido")
            rol_form = AgregarRol(request.POST)
            rol_form.save(commit=True)
            # mensaje = "Permiso \'%s\' creado..\n" % name
            # messages.add_message(request, messages.INFO, mensaje)
            return redirect('agregarRol')# direccion url de la app
        else:
            print("no es valido")
            mensaje = "Error, intente datos diferentes"
            messages.add_message(request, messages.INFO, mensaje)
            rol_form = AgregarRol()  # crea una instancia permiso_form vacia con el constructor PermisoForm()
    else:
        rol_form = AgregarRol()
        return render(request, 'roles/agregarRoles.html', {
            'rol_form': rol_form,
        })
def listarRol(request):

    mensaje = 'Listar Rol'
    messages.add_message(request, messages.INFO, mensaje)
    roles = Group.objects.all()
    return render(request, 'roles/listarRoles.html', {
        'roles': roles
    })

def eliminarRol(request, pk):

    eliminar = Group.objects.get(pk=pk)
    mensaje = "Roles \'%s\' eliminado..\n" % eliminar
    messages.add_message(request, messages.INFO, mensaje)
    eliminar.delete()
    return redirect('../listar')

def editarRol(request, pk):

    mensaje = 'Modificar Permiso'
    messages.add_message(request, messages.INFO, mensaje)
    # mod = Permission.objects.get(pk=pk)
    # editar= Group.objects.get(groud_id=pk)
    editar = Group.objects.get(id=pk)
    # editar_form= EditarPermisos(instance=editar)

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