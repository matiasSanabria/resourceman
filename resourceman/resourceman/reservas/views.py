from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import Permission, User
from django.shortcuts import redirect, render
from .forms import ReservasForm
from ..tipos_recursos.models import Recurso, Estados
from ..reservas.models import Reservas
from django.contrib import messages
import datetime


__author__ = 'hector'
# Create your views here.
def comprobarTime(reserva):

    reservas = Reservas.objects.filter(fecha=reserva.fecha).filter(recurso=reserva.recurso.codigo_recurso)
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
            if comprobarTime(reserva) == True:
                reserva.save()
                return redirect('crear_reserva')
            # print("Recurso no disponible")
        else:
            pass

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
    reservas = Reservas.objects.filter(usuario=request.user).exclude(estado='TE')
    return render(request, 'reservas/listar_reservas_usuario.html', {'reservas': reservas})


@login_required
def listarReservasAdmin(request):

    mensaje = 'Listar Reservas'
    messages.add_message(request, messages.INFO, mensaje)
    reservas = Reservas.objects.all().exclude(estado='TE')
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
    reserva.estado = 'EC'
    reserva.save()
    enuso = Estados.objects.get(descripcion="EN USO")
    recurso.estado = enuso
    recurso.save()
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
    return redirect('../listar/admin')

