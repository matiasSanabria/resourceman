from django.shortcuts import redirect, render
from django.conf import settings
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.core.mail import send_mail

from .forms import *
from ..tipos_recursos.models import Recurso


@login_required
def listar_estados_reclamos(request):
    """
        Permite listar los estados de los reclamos con los siguientes datos

        codigo: 
                        del estado del reclamo que se utiliza como clave primaria
        descripcion: 
                        descripcion del estado del reclamo

        :param request: 
        :return: el formulario para listar los estados de los reclamos
    """
    mensaje = 'Listar Estados'
    messages.add_message(request, messages.INFO, mensaje)
    lista = EstadoReclamo.objects.all()
    return render(request, 'reclamos/listar_estados_reclamo.html', {'lista': lista})


@login_required
def crear_estado_reclamo(request):
    """
        Permite crear un estado de reclamo con los siguientes datos
        codigo: 
                        del estado del reclamo que se utiliza como clave primaria
        descripcion: 
                        descripcion del estado del reclamo
        :param request: 
        :return: el formulario para crear un nuevo estado de reclamo
    """
    if request.method == "POST":
        estado = EstadoReclamoForm(request.POST)
        if estado is not None:
            if estado.is_valid():
                estado.save()
                messages.success(request, "Estado guardado correctamente")
                return redirect('crear_estado')
        else:
            messages.error(request, "Ocurrio un error al guardar el estado. Vuelva a intentarlo")

    estado = EstadoReclamoForm()
    return render(request, 'reclamos/crear_estado_reclamo.html', {'estado': estado})


@login_required
def editar_estado_reclamo(request, codigo):
    """
        Permite editar un estado de reclamo con los siguientes datos
        codigo: 
                        del estado de reclamo que se utiliza como clave primaria
        descripcion: 
                        descripcion del estado de reclamo
        :param request: 
        :return:
    """
    mensaje = 'Modificar Estado'
    messages.add_message(request, messages.INFO, mensaje)
    editar = EstadoReclamo.objects.get(codigo=codigo)

    if request.method == 'POST':
        editar_form = EstadoReclamoForm(request.POST, instance=editar)
        if editar_form.is_valid():
            editar_form.save()
            return redirect('listar_estados')
        else:
            editar_form = EstadoReclamoForm(request.POST, instance=editar)

        return render(request, 'reclamos/editar_estado_reclamo.html', {
            'editar_form': editar_form,
            'codigo': codigo
        })
    else:
        editar_form = EstadoReclamoForm(instance=editar)
        return render(request, 'reclamos/editar_estado_reclamo.html', {
            'editar_form': editar_form,
            'codigo': codigo
        })


@login_required
def eliminar_estado_reclamo(request, codigo):
    """
        Permite eliminar estado de recurso

        nombre nombre: 
                        del estado de recurso a eliminar
        :param request: 
        :return: el formulario para listar los estados de recursos
    """
    eliminar = EstadoReclamo.objects.get(codigo=codigo)
    mensaje = "Estado de Recurso \'%s\' eliminado..\n" % eliminar
    messages.add_message(request, messages.INFO, mensaje)
    eliminar.delete()
    return redirect('../listar_estados')


@login_required
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
            send_mail('Reclamos', mensaje, user.email, [settings.EMAIL_HOST_USER], fail_silently=False)
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
def editar_reclamo(request, pk):
    """
    Metodo para editar un reclamo. Que consiste en cambiar el estado del mismo
    :param request: 
    :param pk: 
    :return: 
    """
    mensaje = 'Editar Reclamo'
    messages.add_message(request, messages.INFO, mensaje)
    # mod = Permission.objects.get(pk=pk)
    editar= Reclamo.objects.get(id=pk)
    # editar_form= EditarPermisos(instance=editar)

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