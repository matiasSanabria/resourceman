
from django.shortcuts import render, redirect, render_to_response

from django.contrib import messages
from .forms import *



from django.shortcuts import render_to_response
from .forms import EditarPermisos, AgregarPermiso, ListarPermisos




def listarPermisos(request):
    formulario = ListarPermisos()
    return render_to_response("permisos/listarPermisos.html", {'formulario': formulario})

def editarPermiso(request):
    formulario = EditarPermisos()
    return render_to_response("permisos/editarPermisos.html", {'formulario':formulario})


def agregarPermiso(request):
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