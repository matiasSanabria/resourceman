from django.shortcuts import render
from ..tipos_recursos.models import TipoRecurso
from ..mantenimiento.forms import MantenimientoForm


def crear_mantenimiento(request):
    """
    Crea un nuevo mantenimiento para un recurso indicado
    :param request: 
    :return: 
    """
    if request.method == "POST":
        mantenimiento = MantenimientoForm(request.POST)
        if mantenimiento.is_valid():
            mantenimiento.save()
            return request('crear_mantenimiento')
        else:
            pass

    mantenimiento = MantenimientoForm()
    return render(request, 'mantenimiento/crear_mantenimiento.html', {'mantenimiento': mantenimiento})
