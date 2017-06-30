from django.contrib.auth.decorators import login_required, permission_required
from django.contrib import messages
from django.shortcuts import render_to_response, render, redirect

from .forms import RegistroUsuarioForm
from .models import RegistroUsuario


@login_required
@permission_required('per_configuracion_registro_usuario')
def submenu_configuraciones(request):
    """
    Muestra el submenu del menu de configuraciones
    :param request:
    :return:
    """
    return render_to_response("configuraciones/menu_configuraciones.html")


@login_required
@permission_required('per_configuracion_registro_usuario')
def registro_usuario(request, id):
    """
    Muestra la plantilla que contiene los datos que seran utilizados para el envio de la notificacion de registro
    de un nuevo usuario
    :param request: 
    :return: 
    """
    if request.method == "POST":
        try:
            registro_usuario = RegistroUsuario.objects.get(id=1)
            registro_usuario_form = RegistroUsuarioForm(request.POST, instance=registro_usuario)

            if registro_usuario_form.is_valid():
                reg = registro_usuario_form.save(commit=False)
                reg.id = 1
                reg.save()
                messages.success(request, "Datos guardados exitosamente")
                return redirect('configuraciones')

            else:
                registro_usuario_form = RegistroUsuarioForm(request.POST, instance=registro_usuario)
                return render(request, 'configuraciones/registro_usuario.html', {'registro_usuario_form': registro_usuario_form})

        except RegistroUsuario.DoesNotExist:
            registro_usuario = RegistroUsuarioForm(request.POST)
            if registro_usuario is not None:
                if registro_usuario.is_valid():
                    reg = registro_usuario.save(commit=False)
                    reg.id = 1
                    reg.save()
                    messages.success(request, "Datos guardados exitosamente")
                    return redirect('configuraciones')
            else:
                messages.error(request, "Ocurrio un error al guardar los datos. Vuelva a intentarlo")

    if request.method == "GET":
        try:
            registro_usuario = RegistroUsuario.objects.get(id=1)

        except RegistroUsuario.DoesNotExist:
            registro_usuario = RegistroUsuarioForm()
            return render(request, 'configuraciones/registro_usuario_inicial.html', {'registro_usuario': registro_usuario})

    registro_usuario_form = RegistroUsuarioForm(instance=registro_usuario)
    return render(request, 'configuraciones/registro_usuario.html', {'registro_usuario_form': registro_usuario_form})
