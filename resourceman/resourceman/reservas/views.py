from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import Permission, User
from django.shortcuts import redirect, render
from .forms import ReservasForm
from ..tipos_recursos.models import Recurso, Estados
from ..reservas.models import Reservas
from django.contrib import messages
from django.core.mail import send_mail
from django.conf import settings
import datetime


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
def listarReservasUser(request):

    mensaje = 'Listar Reservas'
    messages.add_message(request, messages.INFO, mensaje)
    reservas = Reservas.objects.filter(usuario=request.user).exclude(estado='TE'
                                                            ).exclude(estado='CA')
    return render(request, 'reservas/listar_reservas_usuario.html', {'reservas': reservas})


@login_required
def listarReservasAdmin(request):

    mensaje = 'Listar Reservas'
    messages.add_message(request, messages.INFO, mensaje)
    reservas = Reservas.objects.all().filter(tipo_recurso__encargado__usuario=request.user).exclude(estado='TE').exclude(estado='CA')
    return render(request, 'reservas/listar_reservas_admin.html', {'reservas': reservas})


def per_num():
    per = Permission.objects.get(codename='per_listar_reservas')
    return per.id


@login_required
def listarReserva(request):

    usuarios = User.objects.filter(groups__permissions=per_num())
    for u in usuarios:
        if(u.id == request.user.id):
            return redirect('listar_reservas_admin')
    return redirect('listar_reservas_usuarios')


@login_required
def enCurso(request, pk):

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
def devuelto(request, pk):
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
def noDevuelto(request, pk):
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
def cancelado(request, pk):
    reserva = Reservas.objects.get(id=pk)
    if reserva.estado == 'RE':
        user_id = reserva.usuario.id
        user = User.objects.get(id=user_id)
        reserva.estado = 'CA'
        reserva.save()
        mensaje = 'Estimado ' + user.first_name + ' le informamos que la reserva del recurso ' + reserva.recurso.nombre_recurso + ' ha sido cancelada.'
        send_mail('Recurso no devuelto', mensaje, settings.EMAIL_HOST_USER, [user.email], fail_silently=False)
        messages.success(request, "Cancelado")

    return redirect('../listar/user')

