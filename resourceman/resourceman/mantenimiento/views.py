from django.contrib.auth.decorators import login_required
from django.shortcuts import redirect, render

from ..mantenimiento.forms import MantenimientoForm


@login_required
def crear_mantenimiento(request):

    if request.POST == "POST":
        mantenimiento = MantenimientoForm(request.POST)

        if mantenimiento.is_valid():
            mantenimiento.save()
            #return redirect('crear')
        else:
            pass
    else:
        mantenimiento = MantenimientoForm()
    return render(request, 'mantenimiento/crear_mantenimiento.html', {'mantenimiento': mantenimiento})

