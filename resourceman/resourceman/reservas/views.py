from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import Group, Permission, User
from django.shortcuts import redirect, render
# from .models import CaracteristicasRecursos
from .forms import ReservasForm
from django.utils import timezone
from ..tipos_recursos.models import TipoRecurso
from ..reservas.models import Reservas
from django.contrib import messages
from rest_framework.decorators import api_view
from rest_framework.response import Response
import datetime

__author__ = 'hector'
# Create your views here.
@login_required
def crearReserva(request):
    """
    Permite crear una nueva reserva con los siguientes datos

    Recruso:
                    clave del recurso que se reservara
    Inicio:
                    fecha y hora de inicio de reserva
    Fin:
                    fecha y hora de fin de reserva
    usuario:
                    Usuario que realiza la reserva
    :param request:
    :return: el formulario para crear otra reserva
    """
    if request.method == "POST":

        reserva_form = ReservasForm(request.POST)
        print("comprobando datos")
        print("...................inicio................")
        print(reserva_form)
        print("...................fin................")
        if reserva_form.is_valid():
            print("reserva valida")
            reserva = reserva_form.save(commit=False)
            # reserva.fecha_ini = timezone.now
            # reserva.fecha_fin = timezone.now
            reserva.fecha = datetime.datetime.now().date()
            reserva.usuario = request.user

            reserva.save()
            return redirect('crear_reserva')

        else:
            pass

    reserva_form = ReservasForm()
    dicc = {}
    for tipo_recurso in TipoRecurso.objects.all():
        dicc[tipo_recurso.nombre] = [r.codigo_recurso for r in tipo_recurso.recurso_set.filter(estado__descripcion='DISPONIBLE')]
    # reserva.tipo_recurso = TipoRecurso.objets.all()
    return render(
        request, 'reservas/crear_reservas.html', {
        'reserva_form': reserva_form,
        'recursos_por_tipo_recurso': dicc}
    )

@login_required
def listarReservasUser(request):

    mensaje = 'Listar Reservas'
    messages.add_message(request, messages.INFO, mensaje)
    reservas = Reservas.objects.filter(usuario=request.user)
    return render(request, 'reservas/listar_reservas_usuario.html', {'reservas': reservas})

@login_required
def listarReservasAdmin(request):

    mensaje = 'Listar Reservas'
    messages.add_message(request, messages.INFO, mensaje)
    reservas = Reservas.objects.all()
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
