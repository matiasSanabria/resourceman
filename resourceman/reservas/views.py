from django.contrib.auth.decorators import login_required, permission_required
from django.contrib.auth.models import Permission, User
from django.shortcuts import redirect, render
from .forms import ReservasForm, SolicitudForm
from tipos_recursos.models import Recurso, Estados
from usuarios.models import Usuario
from .models import Reservas, SolicitudReservas
from django.contrib import messages
from django.core.mail import send_mail
from django.conf import settings
import datetime
from datetime import date, timedelta

__author__ = 'hector'
# Create your views here.


def comprobarTime(reserva):

    reservas = Reservas.objects.filter(fecha=reserva.fecha).filter(recurso=reserva.recurso.codigo_recurso).exclude(estado='TE')
    for rese in reservas:
            if (reserva.hora_ini < rese.hora_fin) and (reserva.hora_ini > rese.hora_ini):
                return False
            elif (reserva.hora_fin < rese.hora_fin) and (reserva.hora_fin > rese.hora_ini):
                return False
            elif (reserva.hora_ini == rese.hora_ini) and (reserva.hora_fin == rese.hora_fin):
                return False
    return True


@login_required
@permission_required('reservas.per_realizar_reserva')
def crearReserva(request):
    """
    Permite crear una nueva reserva con los siguientes datos

    tipo_recurso: tipo de recurso a reserva

    recruso: clave del recurso que se reservara

    fecha: fecha de reserva

    hora_ini: hora de inicio de reserva

    hora_fin: hora fin de reserva

    usuario: Usuario que realiza la reserva

    descripcion: breve descripcion del uso del recurso

    estado: estado de la reserva


    :param request:
    :return: el formulario para crear otra reserva
    """
    if request.method == "POST":

        reserva_form = ReservasForm(request.POST)
        if reserva_form.is_valid():
            reserva = reserva_form.save(commit=False)
            reserva.fecha = datetime.datetime.now().date()
            reserva.usuario = request.user
            if request.POST.get('recurso'):
                if reserva.hora_ini >= datetime.datetime.strptime('07:00', '%H:%M').time() and reserva.hora_fin <= datetime.datetime.strptime('22:00', '%H:%M').time():
                    if comprobarTime(reserva)== True:
                        if reserva.descripcion:
                            reserva.save()
                            messages.success(request,"Reserva realizada con exito")

                            # res = Reservas.objects.get(id=request.POST.get('reserva'))
                            res = reserva
                            user = User.objects.get(username=request.user)
                            mensaje = 'Hola ' + user.first_name + ' la reserva del recurso: ' + res.recurso.nombre_recurso + ' se ha realizado con exito.\n' + '\nFecha:  ' + res.fecha.strftime('%d/%m/%Y') + '\nDesde las: ' + res.hora_ini.strftime('%H:%M') + ' hasta las ' + res.hora_fin.strftime('%H:%M')
                            send_mail('Reserva', mensaje, settings.EMAIL_HOST_USER, [user.email], fail_silently=False)
                            return redirect('crear_reserva')
                        else:
                            messages.warning(request, "Complete el compo Descripcion")

                    else:
                        messages.warning(request, "Las horas introducidas no son validas")
                else:
                    messages.warning(request, "Las horas de reserva estan establecidas desde las 07:00 hasta las 22:00 seleccione un rango valido.")
            else:
                messages.error(request, "Seleccione un recurso valido")
                messages.warning(request, "Si no le aparece opciones en recursos; no tiene disponible recursos de ese tipo en el horario deseado")

        else:
            messages.error(request, "La reserva no pudo ser realizada. Datos invalidos")
    else:
        reserva_form = ReservasForm()
    return render(
        request, 'reservas/crear_reservas.html', {
        'reserva_form': reserva_form,
        }
    )


@login_required
@permission_required('reservas.per_listar_sus_reservas')
def listarReservasUser(request):
    """
    Permite listar las reservas realizadas por el usuario con los siguientes datos

    nombre del recuros: del recurso reservado

    fecha: fecha de reserva

    inicio: hora de inicio de reserva

    fin: hora del final de la reserva
    estado: indica si el tipo de recurso esta activo o no
    - RE "REALIZADA"
    - CA "CANCELADA"
    - RA "REASIGNADA"
    - EC "EN CURSO"
    - ND "NO DEVUELTO"
    - TE "TERMINADA"
    :param request:
    :return: el formulario para listar reservas
    """
    mensaje = 'Listar Reservas'
    messages.add_message(request, messages.INFO, mensaje)
    reservas = Reservas.objects.filter(usuario=request.user).exclude(estado='TE'
                                                            ).exclude(estado='CA')
    return render(request, 'reservas/listar_reservas_usuario.html', {'reservas': reservas})


@login_required
@permission_required('reservas.per_listar_reservas')
def listarReservasAdmin(request):
    """
    Permite listar las reservas realizadas por el usuario con los siguientes datos

    nombre de usuario: del usuario que realizo la reserva

    nombre del recuros: del recurso reservado

    fecha: fecha de reserva

    inicio: hora de inicio de reserva

    fin: hora del final de la reserva
    estado: indica si el tipo de recurso esta activo o no
    - RE "REALIZADA"
    - RA "REASIGNADA"
    - EC "EN CURSO"
    - ND "NO DEVUELTO"
    :param request:
    :return: el formulario para listar reservas
    """
    mensaje = 'Listar Reservas'
    messages.add_message(request, messages.INFO, mensaje)
    reservas = Reservas.objects.all().filter(tipo_recurso__encargado__usuario=request.user).exclude(estado='TE').exclude(estado='CA')
    return render(request, 'reservas/listar_reservas_admin.html', {'reservas': reservas})


def per_num():
    per = Permission.objects.get(codename='per_listar_reservas')
    return per.id


@login_required
def listarReserva(request):
    """
    Verifica si el usuario logeado tiene permisos para ingresar a listar reservas admin
    de no tenerlo se le mostrara el listar reservas user

    :param request:
    :return: lista corrresponciente al tipo de usuario
    """
    usuarios = User.objects.filter(groups__permissions=per_num())
    for u in usuarios:
        if(u.id == request.user.id):
            return redirect('listar_reservas_admin')
    return redirect('listar_reservas_usuarios')


@login_required
@permission_required('reservas.per_listar_reservas')
def enCurso(request, pk):
    """
    Cambia el estado de la reserva a "EN CURSO", y el estado del recurso a "EN USO" solo si
    el recurso se encuentra disponible
    :param request:
    :param pk: id identificador de reservas
    :return: redireccion a lista de reservas admin
    """
    reserva = Reservas.objects.get(id=pk)
    recu_id = reserva.recurso.codigo_recurso
    recurso = Recurso.objects.get(codigo_recurso=recu_id)
    if recurso.estado.descripcion != "EN USO":
        reserva.estado = 'EC'
        reserva.save()
        enuso = Estados.objects.get(descripcion="EN USO")
        recurso.estado = enuso
        recurso.save()
        messages.success(request, "En curso")
    else:
        messages.warning(request, "El recurso no esta disponible")
    return redirect('../listar/admin')


@login_required
@permission_required('reservas.per_listar_reservas')
def devuelto(request, pk):
    """
    Cambia el estado de la reserva a "TERMINADO", y el estado del recurso a "DISPONIBLE"
    :param request:
    :param pk: id identificador de reservas
    :return: redireccion a lista de reservas admin
    """
    reserva = Reservas.objects.get(id=pk)
    recu_id = reserva.recurso.codigo_recurso
    recurso = Recurso.objects.get(codigo_recurso=recu_id)
    reserva.estado = 'TE'
    reserva.save()
    disponible = Estados.objects.get(descripcion="DISPONIBLE")
    recurso.estado = disponible
    recurso.save()
    messages.success(request, "Devuelto")
    return redirect('../listar/admin')


@login_required
@permission_required('reservas.per_listar_reservas')
def noDevuelto(request, pk):
    """
    Cambia el estado de la reserva a "NO DEVUELTO", y notifica al usuario via correo
    solo si la reserva se encuentra "EN CUROS"
    :param request:
    :param pk: id identificador de reservas
    :return: redireccion a lista de reservas admin
    """
    reserva = Reservas.objects.get(id=pk)
    if reserva.estado == 'EC':
        user_id = reserva.usuario.id
        user = User.objects.get(id=user_id)
        reserva.estado = 'ND'
        reserva.save()
        mensaje = 'Estimado ' + user.first_name + ' le informamos que su tiempo de reserva del recurso ' + reserva.recurso.nombre_recurso + ' ha culminado, por favor devolverlo cuanto antes.'
        send_mail('Recurso no devuelto', mensaje, settings.EMAIL_HOST_USER, [user.email], fail_silently=False)
        messages.success(request, "Usuario Informado")
    return redirect('../listar/admin')


@login_required
@permission_required('reservas.per_cancelar_reserva')
def cancelado(request, pk):
    """
    Cambia el estado de la reserva a "CANCELADO", solo si el mismo se encontraba en
    "REALIZADO" se envia una confirmacion dde la reserva por correo
    :param request:
    :param pk: id identificador de reservas
    :return: redireccion a lista de reservas user
    """
    reserva = Reservas.objects.get(id=pk)
    if reserva.estado == 'RE':
        user_id = reserva.usuario.id
        user = User.objects.get(id=user_id)
        reserva.estado = 'CA'
        reserva.save()
        mensaje = 'Estimado ' + user.first_name + ' le informamos que la reserva del recurso ' + reserva.recurso.nombre_recurso + ' ha sido cancelada.'
        send_mail('Reserva Cancelada', mensaje, settings.EMAIL_HOST_USER, [user.email], fail_silently=False)
        messages.success(request, "Cancelado")

    return redirect('../listar/user')

@login_required
@permission_required('reservas.per_solicitar_reserva')
def solicitarReserva(request):
    """
    Permite crear una nueva solicitud de reserva con los siguientes datos

    tipo_recurso: tipo de recurso a reserva

    recruso: clave del recurso que se reservara

    fecha_solicitud: fecha en la que se realizo la solicitud

    fecha_reserva: fecha de reserva

    hora_ini: hora de inicio de reserva

    hora_fin: hora fin de reserva

    usuario: Usuario que realiza la reserva

    descripcion: breve descripcion del uso del recurso

    estado: estado de la solicitud


    :param request:
    :return: el formulario para crear otra reserva
    """
    if request.method == "POST":

        solicitud_form = SolicitudForm(request.POST)
        if solicitud_form.is_valid():
            solicitud = solicitud_form.save(commit=False)
            solicitud.fecha_solicitud = datetime.datetime.now()
            solicitud.usuario = request.user
            if request.POST.get('recurso'):
                if solicitud.hora_ini >= datetime.datetime.strptime('07:00', '%H:%M').time() and solicitud.hora_fin <= datetime.datetime.strptime('22:00', '%H:%M').time() and solicitud.hora_ini < solicitud.hora_fin:
                    inicio = date.today() + timedelta(days=2)
                    limite = date.today() + timedelta(days=15)
                    if solicitud.fecha_reserva > inicio and solicitud.fecha_reserva < limite:
                        if solicitud.descripcion:
                            solicitud.estado='PP'
                            solicitud.save()
                            messages.success(request,"Solicitud realizada con exito")

                            sol = solicitud
                            user = User.objects.get(username=request.user)
                            # mensaje = 'Hola ' + user.first_name + ' la solicitud del recurso: ' + sol.recurso.nombre_recurso + ' se ha realizado con exito.\n' + '\nFecha:  ' + sol.fecha_reserva.strftime('%d/%m/%Y') + '\nDesde las: ' + sol.hora_ini.strftime('%H:%M') + ' hasta las ' + sol.hora_fin.strftime('%H:%M')
                            # send_mail('Solicitud de Reserva', mensaje, settings.EMAIL_HOST_USER, [user.email], fail_silently=False)
                            return redirect('listar_solicitudes')

                        else:
                            messages.warning(request, "Complete el compo Descripcion")
                    else:
                        messages.warning(request, "Fecha seleccionada invalida!!")

                else:
                    messages.warning(request, "Las horas de reserva estan establecidas desde las 07:00 hasta las 22:00 seleccione un rango valido.")
            else:
                messages.error(request, "Seleccione un recurso valido")
                messages.warning(request, "Si no le aparece opciones en recursos; no tiene disponible recursos de ese tipo")

        else:
            messages.error(request, "La solicitud no pudo ser realizada. Datos invalidos")
    else:
        solicitud_form = SolicitudForm()
    return render(
        request, 'reservas/crear_solicitud.html', {
        'solicitud_form': solicitud_form,
        }
    )


@login_required
@permission_required('reservas.per_listar_sus_solicitudes_reservas')
def listarSolicitudes(request):
    """
    Permite listar las solicitudes de reservas reservas realizadas por el usuario con los siguientes datos

    nombre del recuros: del recurso reservado

    fecha_solicitud: fecha y hora de solicitud

    fecha_reserva: fecha de reserva

    inicio: hora de inicio de reserva

    fin: hora del final de la reserva

    estado:
    - PP "POR PROCESAR"
    - CA "CANCELADA"
    - CO "CONCLUIDA"

    :param request:
    :return: el formulario para listar solicitudes
    """
    mensaje = 'Listar Solicitudes de Reservas'
    messages.add_message(request, messages.INFO, mensaje)
    solicitudes = SolicitudReservas.objects.filter(usuario=request.user).exclude(estado='CO'
                                                                     ).exclude(estado='CA')
    return render(request, 'reservas/listar_solicitudes.html', {'solicitudes': solicitudes})



@login_required
@permission_required('reservas.per_listar_solicitudes_reservas')
def listarSolicitudesAdmin(request):
    """
    Permite listar las solicitudes de reservas realizadas con los siguientes datos

    nombre del recuros: del recurso reservado

    fecha_solicitud: fecha y hora de solicitud

    fecha_reserva: fecha de reserva

    inicio: hora de inicio de reserva

    fin: hora del final de la reserva
    estado:
    - PP "POR PROCESAR"
    - CA "CANCELADA"
    - CO "CONCLUIDA"

    :param request:
    :return: el formulario para listar solicitudes
    """
    mensaje = 'Listar Solicitudes de Reservas'
    messages.add_message(request, messages.INFO, mensaje)
    solicitudes = SolicitudReservas.objects.all().exclude(estado='CO'
                                                                     ).exclude(estado='CA')
    return render(request, 'reservas/listar_solicitudes_admin.html', {'solicitudes': solicitudes})


@login_required
@permission_required('reservas.per_cancelar_solicitud_reserva')
def cancelarSolicitud(request, pk):
    """
    Cambia el estado de la solicitud de reserva a "CANCELADO", solo si el mismo se encontraba en
    "POR PROCESAR"
    :param request:
    :param pk: id identificador de la solicitud de reservas
    :return: redireccion a lista de solicitudes de reservas user

    """
    solicitud = SolicitudReservas.objects.get(id=pk)
    if solicitud.estado == 'PP':
        user_id = solicitud.usuario.id
        user = User.objects.get(id=user_id)
        solicitud.estado = 'CA'
        solicitud.save()
        # mensaje = 'Estimado ' + user.first_name + ' le informamos que su solicitud de reserva del recurso ' + solicitud.recurso.nombre_recurso + ' ha sido cancelada.'
        # send_mail('Cancelacion de Solicitud', mensaje, settings.EMAIL_HOST_USER, [user.email], fail_silently=False)
        messages.success(request, "Cancelado")

    return redirect('../listar/solicitudes')

