from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect

from ..tipos_recursos.models import Estados, Recurso
from ..mantenimiento.forms import MantenimientoForm


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

            mantenimiento.save()
            return redirect('crear_mantenimiento')
        else:
            pass

    mantenimiento = MantenimientoForm()
    return render(request, 'mantenimiento/crear_mantenimiento.html', {'mantenimiento': mantenimiento})
