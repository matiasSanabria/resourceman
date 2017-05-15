from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from django.shortcuts import render

from ..mantenimiento.forms import MantenimientoForm
from ..mantenimiento.models import Mantenimiento


@login_required
def crear_mantenimiento(request):
    if request.method == "POST":
        recurso = request.POST['recurso']
        motivo = request.POST['motivo']
        tipo_mantenimiento = request.POST['tipo_mantenimiento']
        fecha_inicio = request.POST['fecha_inicio']
        fecha_fin = request.POST['fecha_fin']
        mantenimiento_programado = request.POST['mantenimiento_programado']
        costo = request.POST['costo']

        Mantenimiento.objects.create(
            recurso=recurso,
            motivo=motivo,
            tipo_mantenimiento=tipo_mantenimiento,
            fecha_inicio=fecha_inicio,
            fecha_fin=fecha_fin,
            mantenimiento_programado=mantenimiento_programado,
            costo=costo
        )
        return HttpResponse('')

    mantenimiento = MantenimientoForm()
    return render(request, 'mantenimiento/crear_mantenimiento.html', {'mantenimiento': mantenimiento})
