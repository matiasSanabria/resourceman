import django.shortcuts
from django.contrib import messages
from .forms import *


def crear_reclamo(request):
    # fecha = forms.DateField(widget=SelectDateWidget(), initial=(timezone.now()))
    if request.method == "POST":
        # aquí código que guarda el formulario en la bd :)
        crear_reclamo = CrearReclamo(request.POST)
        if crear_reclamo.is_valid():
            crear_reclamo.save()

            mensaje = "Se ha hecho el reclamo, gracias..\n"
            messages.add_message(request, messages.INFO, mensaje)
        else:
            mensaje = "Los datos ingresados no son validos..\n"
            messages.add_message(request, messages.INFO, mensaje)

        crear_reclamo = CrearReclamo(instance=None)
        return django.shortcuts.render(request, 'reclamos/crear_reclamo.html', {
            'crear_reclamo': crear_reclamo,
        })
    else:
        crear_reclamo = CrearReclamo(instance=None)
        return django.shortcuts.render(request, 'reclamos/crear_reclamo.html', {
            'crear_reclamo': crear_reclamo,
        })


def list_reclamo(request):
    """
    Funcion que permite listar todos los roles existentes.
    :param request:
    :return:
    """
    mensaje = 'Listar Reclamos'
    messages.add_message(request, messages.INFO, mensaje)
    reclamos = Reclamo.objects.all()
    return django.shortcuts.render(request, 'reclamos/listar_reclamos.html', {
        'reclamos': reclamos
    })


def ver_reclamo(request, pk):
    mensaje = 'Ver Reclamo'
    messages.add_message(request, messages.INFO, mensaje)
    reclamo = Reclamo.objects.get(pk=pk)
    return django.shortcuts.render(request, 'reclamos/ver_reclamo.html', {
        'reclamo': reclamo,
        'pk': pk
    })

def editar_reclamo(request, pk):

    mensaje = 'Editar Reclamo'
    messages.add_message(request, messages.INFO, mensaje)
    # mod = Permission.objects.get(pk=pk)
    editar= Reclamo.objects.get(id=pk)
    # editar_form= EditarPermisos(instance=editar)

    if request.method == 'POST':
        editar_form = EditarReclamo(request.POST, instance=editar)
        if editar_form.is_valid():
            editar_form.save()
            return django.shortcuts.redirect('listarReclamos')
        else:
            editar_form = EditarReclamo(request.POST, instance=editar)

            return django.shortcuts.render(request, 'reclamos/editar_reclamo.html', {
            'editar_form': editar_form,
            'pk': pk
        })
    else:
        editar_form = EditarReclamo(instance=editar)
        return django.shortcuts.render(request, 'reclamos/editar_reclamo.html', {
            'editar_form': editar_form,
            'pk': pk
        })