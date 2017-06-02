from django.shortcuts import redirect, render
from django.contrib import messages
from django.contrib.auth.decorators import login_required, permission_required

from .forms import *
from tipos_recursos.models import Recurso


@login_required
@permission_required('reclamos.per_crear_reclamo')
def crear_reclamo(request):
    """
    Metodo que permite la creacion de reclamos y el envio de un correo al encargado.
    :param request: 
    :return: 
    """
    if request.method == "POST":
        # aquí código que guarda el formulario en la bd :)
        crear_reclamo = CrearReclamo(request.POST)
        if crear_reclamo.is_valid():
            reclamo = crear_reclamo.save(commit=False)
            reclamo.usuario = request.user
            reclamo.estado = 'N'
            reclamo.save()

            mensaje = "Se ha hecho el reclamo, gracias..\n"
            messages.add_message(request, messages.INFO, mensaje)

            # apartado para el envio de las notificaciones de reclamos al administrador
            rec = Recurso.objects.get(codigo_recurso=request.POST.get('recurso'))
            mensaje = 'Tipo de Recurso: ' + rec.tipo_recurso.nombre + '\nRecurso: ' + rec.codigo_recurso + '\nObs: ' + request.POST.get('descripcion')

            # obtenemos el correo del usuario logueado
            user = User.objects.get(username=request.user)
            #send_mail('Reclamos', mensaje, user.email, [settings.EMAIL_HOST_USER], fail_silently=False)
        else:
            mensaje = "Los datos ingresados no son validos..\n"
            messages.add_message(request, messages.INFO, mensaje)

        crear_reclamo = CrearReclamo(instance=None)
        return render(request, 'reclamos/crear_reclamo.html', {
            'crear_reclamo': crear_reclamo,
        })
    else:
        crear_reclamo = CrearReclamo(instance=None)
        return render(request, 'reclamos/crear_reclamo.html', {
            'crear_reclamo': crear_reclamo,
        })


@login_required
@permission_required('reclamos.per_listar_reclamos')
def list_reclamo(request):
    """
    Funcion que permite listar todos los roles existentes.
    :param request:
    :return:
    """
    mensaje = 'Listar Reclamos'
    messages.add_message(request, messages.INFO, mensaje)
    reclamos = Reclamo.objects.all()
    return render(request, 'reclamos/listar_reclamos.html', {
        'reclamos': reclamos
    })


@login_required
@permission_required('reclamos.per_ver_reclamo')
def ver_reclamo(request, pk):
    """
    Metodo que permite ver un reclamo sin editarlo
    :param request: 
    :param pk: 
    :return: 
    """
    mensaje = 'Ver Reclamo'
    messages.add_message(request, messages.INFO, mensaje)
    reclamo = Reclamo.objects.get(pk=pk)
    return render(request, 'reclamos/ver_reclamo.html', {
        'reclamo': reclamo,
        'pk': pk
    })


@login_required
@permission_required('reclamos.per_modificar_reclamo')
def editar_reclamo(request, pk):
    """
    Metodo para editar un reclamo. Que consiste en cambiar el estado del mismo
    :param request: 
    :param pk: 
    :return: 
    """
    mensaje = 'Editar Reclamo'
    messages.add_message(request, messages.INFO, mensaje)
    editar= Reclamo.objects.get(id=pk)

    if request.method == 'POST':
        editar_form = EditarReclamo(request.POST, instance=editar)
        if editar_form.is_valid():
            editar_form.save()
            return redirect('listarReclamos')
        else:
            editar_form = EditarReclamo(request.POST, instance=editar)

            return render(request, 'reclamos/editar_reclamo.html', {
            'editar_form': editar_form,
            'pk': pk
        })
    else:
        editar_form = EditarReclamo(instance=editar)
        return render(request, 'reclamos/editar_reclamo.html', {
            'editar_form': editar_form,
            'pk': pk
        })