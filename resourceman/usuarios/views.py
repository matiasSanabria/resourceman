

from django.shortcuts import render, redirect, render_to_response
from django.contrib import messages
from django.contrib.auth.models import User
from django.template import RequestContext
from .forms import *
from .models import Usuario, PrioridadUsuario
import datetime

from django.contrib.auth.models import Group, Permission

from django.shortcuts import render


from .forms import UsuarioCreationForm,UsuarioDetalleForm, AgregarPrioridad
from django.contrib.auth.models import Group, Permission
from django.contrib import messages
from django.contrib.auth.models import User, Group
from django.shortcuts import render, redirect, render_to_response
# Create your views here.
def crearUsuario(request):

    if request.method == "POST":
        user_form = UsuarioCreationForm(request.POST)
        user_detail_form = UsuarioDetalleForm(request.POST)
        print("GRUPO")
        print(request.POST.get('groups'))
        if user_form.is_valid():
            if user_detail_form.is_valid():
                user = user_form.save(commit=False)  # guarda en la base de datos.

                user.is_active = 1
                user.save()

                # guardando relacion group user
                g1 = Group.objects.get(id=request.POST.get('groups'))
                print(g1.name)
                print("Username")
                user1 = User.objects.get(username=request.POST.get('username'))
                print(user1.username)

                user1.groups.add(g1)

                user_detail = user_detail_form.save(commit=False)  # guarda en el objeto model, sin guardarlo en la BD.
                user_detail.usuario = user  # asocia de detalle al usuario.
                user_detail.save()  # guarda en BD.
                messages.add_message(request, messages.SUCCESS,
                                     "Usuario -%s- ha sido creado correctamente." % user.username)
                return redirect('agregarUsuario')

    else:
        user_form = UsuarioCreationForm()
        user_detail_form = UsuarioDetalleForm()

    return render(request, 'usuario/crear_usuario.html', {
        'user_form': user_form,
        'user_detail_form': user_detail_form,
    })

def listarUsuario(request):

    mensaje = 'Listar Usuario'
    messages.add_message(request, messages.INFO, mensaje)
    usuario = User.objects.all().order_by('pk')
    detalle_usuario = Usuario.objects.all().order_by('pk')

    print(usuario.count())
    print(detalle_usuario.count())
    if usuario.count() == 1 and detalle_usuario.count() == 0:
        print("aqui")
        new_detail_for_admin = Usuario.objects.create(usuario=usuario.first())
        new_detail_for_admin.save()
        detalle_usuario = Usuario.objects.all().order_by('pk')
    zipped_user_data = zip(usuario, detalle_usuario)
    return render(request, 'usuario/listarUsuarios.html', {
        'zipped_user_data': zipped_user_data, })
        # 'usuario':usuario,'detalle_usuario':detalle_usuario,})

    # return render(request, 'usuario/listarPrioridad.html', {
    #     'prioridades': prioridades
    # })

def editarUsuario(request, username):
    # messages.add_message(request, messages.INFO, "Obs: Para eliminar un usuario, desactive la casilla 'Activo'.")
    # if request.user.is_superuser:
    #     # Para prevenir que se indique manualmente en la url un nombre de usuario accidental o aleatoriamente.
    #     user = get_object_or_404(User, username=username)
        user = User.objects.get(username=username)
        if Usuario.objects.filter(usuario=user).exists():
            # print("existe detalle de usuario.")
            user_detail = Usuario.objects.get(usuario=user)
        else:
            # print("no existe detalle. creando uno nuevo.")
            # Superusuarios creado por línea de comando, no tienen asociado un detalle al comienzo.
            user_detail = Usuario.objects.create(usuario=user)

        if request.method == 'POST':
            # if request.user.is_superuser:
            print("post")
            user_form = UserInfoForm(request.POST, instance=user)
            user_detail_form = UsuarioInfoForm(request.POST, instance=user_detail)

            if user_form.is_valid():
                # print("user form valido")
                if user_detail_form.is_valid():
                    # print("formularios validos")
                    user = user_form.save()  # actualiza la tabla de usuario en la bd.
                    user_detail = user_detail_form.save(commit=False)  # actualiza en el model, sin guardar en BD.
                    user_detail.user = user  # actualiza (por seguridad) el campo de relación.
                    user_detail.save()  # actualiza detalle en la BD.
                    messages.add_message(request, messages.SUCCESS,
                                         "Información del usuario -%s- se ha modificado correctamente." % user.username)
                    # print("mensaje. redirigirá al home.")
                    return redirect('listarUsuario')
                    # else:
                    #     messages.add_message(request, messages.ERROR, "Usted no tiene permisos suficientes para efectuar la operación.")
                    #     return redirect('sar:home')
        else:
            print("get")
            user_form = UserInfoForm(instance=user)
            user_detail_form = UsuarioInfoForm(instance=user_detail)

        return render(request, 'usuario/editarUsuario.html', {
            'user_form': user_form,
            'user_detail_form': user_detail_form,
            'username': user.username,
        })
    # else:
    #     raise Http404('Recurso solicitano no existe. (en realidad, se está impidiendo acceder a esta url porque no'
    #                   ' es superusuario. borrar todo el paréntesis después.)')

def agregarPrioridad(request):
    mensaje = 'Crear Prioridad'
    messages.add_message(request, messages.INFO, mensaje)

    if request.method == 'POST':

        if AgregarPrioridad(request.POST).is_valid():
            print("si es valido")
            prioridad_form = AgregarPrioridad(request.POST)
            prioridad_form.save(commit=True)
            # mensaje = "Prioridad \'%s\' creado..\n" % prioridad_form.codigo
            # messages.add_message(request, messages.INFO, mensaje)
            return redirect('agregarPrioridad')  # direccion url de la app
        else:
            print("no es valido")
            mensaje = "Error, intente datos diferentes"
            messages.add_message(request, messages.INFO, mensaje)
            prioridad_form = AgregarPrioridad()  # crea una instancia permiso_form vacia con el constructor PermisoForm()
    else:
        prioridad_form = AgregarPrioridad()
        return render(request, 'usuario/agregarPrioridad.html', {
            'prioridad_form': prioridad_form,
        })

def listarPrioridad(request):

    mensaje = 'Listar Prioridad'
    messages.add_message(request, messages.INFO, mensaje)
    prioridades = PrioridadUsuario.objects.all()
    return render(request, 'usuario/listarPrioridad.html', {
        'prioridades': prioridades
    })

def editarPrioridad(request, codigo):

    mensaje = 'Modificar Prioridad'
    messages.add_message(request, messages.INFO, mensaje)
    # mod = Permission.objects.get(pk=pk)
    editar= PrioridadUsuario.objects.get(codigo=codigo)
    # editar_form= EditarPermisos(instance=editar)

    if request.method == 'POST':
        editar_form = EditarPrioridad(request.POST, instance=editar)
        if editar_form.is_valid():
            editar_form.save()
            return redirect('listarPrioridad')
        else:
            editar_form = EditarPrioridad(request.POST, instance=editar)

        return render(request, 'usuario/editarPrioridad.html', {
            'editar_form': editar_form,
            'codigo': codigo
        })
    else:
        editar_form = EditarPrioridad(instance=editar)
        return render(request, 'usuario/editarPrioridad.html', {
            'editar_form': editar_form,
            'codigo': codigo
        })