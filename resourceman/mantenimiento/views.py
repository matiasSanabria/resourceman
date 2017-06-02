from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect

from mantenimiento.models import Mantenimiento
from tipos_recursos.models import Estados, Recurso
from mantenimiento.forms import MantenimientoForm


@login_required
def crear_mantenimiento(request):
    """
    Crea un nuevo mantenimiento para un recurso indicado
    :param request: 
    :return: 
    """
    if request.method == "POST":
        mantenimiento = MantenimientoForm(request.POST)
        if mantenimiento.is_valid():
            # obtenemos el objeto de la base de datos del recurso cuyo estado sera modificado
            # para entrar al mantenimiento
            recurso = Recurso.objects.get(codigo_recurso=request.POST.get('recurso'))
            recurso.estado = Estados.objects.get(codigo='MAN')
            recurso.save()

            mantenimiento.tipo_mantenimiento = 'COR'
            mantenimiento.save()
            messages.success(request, "Mantenimiento guardado correctamente")
            return redirect('crear_mantenimiento')
        else:
            messages.error(request, "Ocurrio un error al guardar el mantenimiento")
            pass

    mantenimiento = MantenimientoForm()
    return render(request, 'mantenimiento/crear_mantenimiento.html', {'mantenimiento': mantenimiento})


@login_required
def listar_mantenimientos(request):
    """
    Muestra la lista de mantenimientos en curso del sistema
    :param request: 
    :return: 
    """
    mensaje = 'Listar mantenimientos'
    messages.add_message(request, messages.INFO, mensaje)
    mantenimientos = Mantenimiento.objects.all().exclude(estado='FIN')
    return render(request, 'mantenimiento/listar_mantenimientos.html', {'mantenimientos': mantenimientos})


@login_required
def terminar_mantenimiento(request, id):
    """
    Cambia el estado del mantenimiento a terminado y pone el estado del recurso
    a disponible
    :param request: 
    :return: 
    """
    mantenimiento = Mantenimiento.objects.get(id=id)

    if mantenimiento.estado == "INI":
        mantenimiento.estado = 'FIN'
        recurso = Recurso.objects.get(nombre_recurso=mantenimiento.recurso)
        recurso.estado = Estados.objects.get(codigo="DIS")
        mantenimiento.recurso = recurso
        recurso.save()
        mantenimiento.save()
        messages.success(request, "El mantenimiento ha finalizado")
    else:
        messages.warning(request, "El mantenimiento aun no ha iniciado")

    return redirect('../listar')


@login_required
def recurso_fuera_uso(request, id):
    """
    Cambia el estado del mantenimiento a terminado y pone el estado del recurso
    a disponible
    :param request: 
    :return: 
    """
    mantenimiento = Mantenimiento.objects.get(id=id)

    if mantenimiento.estado == "INI":
        mantenimiento.estado = 'FIN'
        recurso = Recurso.objects.get(nombre_recurso=mantenimiento.recurso)
        recurso.estado = Estados.objects.get(codigo="FUS")
        recurso.activo = 'I'
        mantenimiento.recurso = recurso
        recurso.save()
        mantenimiento.save()
        messages.success(request, "El mantenimiento ha finalizado. El recurso ha pasado a fuera de uso")
    else:
        messages.warning(request, "El mantenimiento aun no ha iniciado")

    return redirect('../listar')