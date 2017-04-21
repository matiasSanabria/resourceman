from django.contrib.auth.decorators import login_required
from django.shortcuts import redirect, render
from .forms import RecursoForm

__author__ = 'matt'

@login_required
def crear(request):
    if request.method == "POST":
        recurso = RecursoForm(request.POST)
        if recurso.is_valid():
            recurso.save()
            return redirect('recurso/crear_recuro.html')
        else:
            pass
    recurso = RecursoForm()
    return render(request, 'recurso/crear_recurso.html', {'recurso': recurso})
