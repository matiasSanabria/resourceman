from django.contrib.auth.decorators import login_required
from django.shortcuts import redirect, render
from .forms import TipoRecursoForm, EstadoForm, RecursoForm
from .models import TipoRecurso, Estados, Recurso
from django.contrib import messages

__author__ = 'matt'

@login_required
def crear(request):
    if request.method == "POST":
        tipo_recurso = TipoRecursoForm(request.POST)
        if tipo_recurso.is_valid():
            tipo_recurso.save()
            return redirect('crear')
        else:
            pass
    tipo_recurso = TipoRecursoForm()
    return render(request, 'tipo_recurso/crear_tipos_recursos.html', {'tipo_recurso': tipo_recurso})


@login_required
def editar(request, nombre):
    mensaje = 'Modificar Tipo de Recurso'
    messages.add_message(request, messages.INFO, mensaje)
    editar = TipoRecurso.objects.get(nombre=nombre)

    if request.method == 'POST':
        editar_form = TipoRecursoForm(request.POST, instance=editar)
        if editar_form.is_valid():
            editar_form.save()
            return redirect('listar')
        else:
            editar_form = TipoRecursoForm(request.POST, instance=editar)

        return render(request, 'tipo_recurso/editar_tipo_recurso.html', {
            'editar_form': editar_form,
            'nombre': nombre
        })
    else:
        editar_form = TipoRecursoForm(instance=editar)
        return render(request, 'tipo_recurso/editar_tipo_recurso.html', {
            'editar_form': editar_form,
            'nombre': nombre
        })


@login_required
def eliminar(request, nombre):
    eliminar = TipoRecurso.objects.get(nombre=nombre)
    mensaje = "Tipo de Recurso \'%s\' eliminado..\n" % eliminar
    messages.add_message(request, messages.INFO, mensaje)
    eliminar.delete()
    return redirect('../listar')


@login_required
def listar_tipos_recursos(request):
    mensaje = 'Listar Permisos'
    messages.add_message(request, messages.INFO, mensaje)
    lista = TipoRecurso.objects.filter(estado='A')
    return render(request, 'tipo_recurso/listar_tipos_recursos.html', {'lista': lista})


########################################################################################################################
@login_required
def listar_estados(request):
    mensaje = 'Listar Estados'
    messages.add_message(request, messages.INFO, mensaje)
    lista = Estados.objects.all()
    return render(request, 'estados/listar_estados.html', {'lista': lista})


@login_required
def crear_estado(request):
    if request.method == "POST":
        estado = EstadoForm(request.POST)
        if estado.is_valid():
            estado.save()
            return redirect('crear_estado')
        else:
            pass
    estado = EstadoForm()
    return render(request, 'estados/crear_estado.html', {'estado': estado})


@login_required
def editar_estado(request, codigo):
    mensaje = 'Modificar Estado'
    messages.add_message(request, messages.INFO, mensaje)
    editar = Estados.objects.get(codigo=codigo)

    if request.method == 'POST':
        editar_form = EstadoForm(request.POST, instance=editar)
        if editar_form.is_valid():
            editar_form.save()
            return redirect('listar_estados')
        else:
            editar_form = EstadoForm(request.POST, instance=editar)

        return render(request, 'estados/editar_estado.html', {
            'editar_form': editar_form,
            'codigo': codigo
        })
    else:
        editar_form = EstadoForm(instance=editar)
        return render(request, 'estados/editar_estado.html', {
            'editar_form': editar_form,
            'codigo': codigo
        })

@login_required
def eliminar_estado(request, codigo):
    eliminar = Estados.objects.get(codigo=codigo)
    mensaje = "Estado de Recurso \'%s\' eliminado..\n" % eliminar
    messages.add_message(request, messages.INFO, mensaje)
    eliminar.delete()
    return redirect('../listar_estados')

########################################################################################################################

@login_required
def crear_recurso(request):
    if request.method == "POST":
        recurso = RecursoForm(request.POST)
        if recurso.is_valid():
            recurso.save()
            return redirect('crear_recurso')
        else:
            pass
    recurso = RecursoForm()
   # caracteristicas = TipoRecurso.lista_caracteristicas(request.TipoRecurso.nombre)
    return render(request, 'recurso/crear_recurso.html', {'recurso': recurso})

@login_required
def editar_recurso(request, codigo_recurso):
    mensaje = 'Modificar Recurso'
    messages.add_message(request, messages.INFO, mensaje)
    editar = Recurso.objects.get(codigo_recurso=codigo_recurso)

    if request.method == 'POST':
        editar_form = RecursoForm(request.POST, instance=editar)
        if editar_form.is_valid():
            editar_form.save()
            return redirect('listar_recursos')
        else:
            editar_form = TipoRecursoForm(request.POST, instance=editar)

        return render(request, 'recurso/editar_recurso.html', {
            'editar_form': editar_form,
            'codigo_recurso': codigo_recurso
        })
    else:
        editar_form = RecursoForm(instance=editar)
        return render(request, 'recurso/editar_recurso.html', {
            'editar_form': editar_form,
            'codigo_recurso': codigo_recurso
        })


@login_required
def eliminar_recurso(request, codigo):
    eliminar = Recurso.objects.get(codigo_recurso=codigo)
    mensaje = "Recurso \'%s\' eliminado..\n" % eliminar
    messages.add_message(request, messages.INFO, mensaje)
    eliminar.delete()
    return redirect('../listar_recursos')


@login_required
def listar_recursos(request):
    mensaje = 'Listar Recursos'
    messages.add_message(request, messages.INFO, mensaje)
    lista = Recurso.objects.all()
    return render(request, 'recurso/listar_recursos.html', {'lista': lista})
