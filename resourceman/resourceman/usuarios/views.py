from django.conf import settings
from django.contrib.auth.decorators import login_required, permission_required
from django.core.mail import send_mail
from .forms import *
from .models import Usuario, PrioridadUsuario
from .forms import UsuarioCreationForm, UsuarioDetalleForm, AgregarPrioridad
from django.contrib import messages
from django.contrib.auth.models import User, Group
from django.shortcuts import render, redirect
from ..configuraciones.models import RegistroUsuario

__author__ = 'hector'


# Create your views here.
@login_required
@permission_required('usuarios.per_crear_usuario')
def crearUsuario(request):
    """
        Página para la creacion de Usuarios.

        Recibe los datos suministrados por el usuario a traves de un post.

        Se definen objetos de User y Usuario para guardar los datos a traves de las funciones del form.

    """
    if request.method == "POST":
        user_form = UsuarioCreationForm(request.POST)
        user_detail_form = UsuarioDetalleForm(request.POST)
        if user_form.is_valid():
            if user_detail_form.is_valid():
                user = user_form.save(commit=False)  # guarda en la base de datos.

                user.is_active = 1
                user.save()

                # guardando relacion group user
                g1 = Group.objects.get(id=request.POST.get('groups'))

                user1 = User.objects.get(username=request.POST.get('username'))
                user1.groups.add(g1)

                user_detail = user_detail_form.save(commit=False)  # guarda en el objeto model, sin guardarlo en la BD.
                user_detail.usuario = user  # asocia de detalle al usuario.
                user_detail.save()  # guarda en BD.
                messages.add_message(request, messages.SUCCESS,
                                     "Usuario -%s- ha sido creado correctamente." % user.username)

                # a partir de aqui se realiza la gestion para el envio del correo al usuario
                # para indicarle que el registro se realizo y que puede acceder al sistema con
                # los datos que se le proveen

                plantilla = RegistroUsuario.objects.get(id=1) #obtenemos los datos de la plantilla que tenemos en la BD
                mensaje = plantilla.mensaje + '\nUsuario: ' + request.POST.get('username') + '\nContraseña: ' + request.POST.get('password1')
                send_mail(plantilla.asunto, mensaje, settings.EMAIL_HOST_USER, [user.email], fail_silently=False)

                return redirect('listarUsuario')

    else:
        user_form = UsuarioCreationForm()
        user_detail_form = UsuarioDetalleForm()

    return render(request, 'usuario/crear_usuario.html', {
        'user_form': user_form,
        'user_detail_form': user_detail_form,
    })

@login_required
@permission_required('usuarios.per_listar_usuario')
def listarUsuario(request):
    """
        Página para listar de Usuario.

        Genera una instancia de los objetos de User, Usuario y luego los devuleve al template listarUsuario.html

    """
    mensaje = 'Listar Usuario'
    messages.add_message(request, messages.INFO, mensaje)
    user = User.objects.all().order_by('pk')
    usuario = user[1:]
    detalle_usuario = Usuario.objects.all().order_by('usuario')

    if usuario.count() == 2 and detalle_usuario.count() == 0:
        new_detail_for_admin = Usuario.objects.create(usuario=usuario.first())
        new_detail_for_admin.save()
        detalle_usuario = Usuario.objects.all().order_by('pk')
    zipped_user_data = zip(usuario, detalle_usuario)
    return render(request, 'usuario/listarUsuarios.html', {
        'zipped_user_data': zipped_user_data, })


@login_required
@permission_required('usuarios.per_editar_usuario')
def editarUsuario(request, username):

        user = User.objects.get(username=username)
        """
                Página para la edicion de Usuario.

                Recibe un Post con un atributo username del usuario a editar.

                Se instancian los objetos User y Usuario con el identificador suministrado.

                Se alteran los datos con el Post recibido y se guardan.

        """
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


@login_required
def eliminarUsuario(request, username):
    user = User.objects.get(username=username)
    user.is_active = 0
    user.save()

    messages.add_message(request, messages.INFO, "Usuario -%s- eliminado exitosamente" % user.username)

    return redirect('listarUsuario')


@login_required
@permission_required('usuarios.per_agregar_prioridad')
def agregarPrioridad(request):
    """
        Página para la agregacion de Prioridad.

        Recibe los datos suministrados por el usuario a traves de un post.

        Se define un objeto para guardar los datos a traves de la funcion del form.

    """
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


@login_required
@permission_required('usuarios.per_listar_prioridad')
def listarPrioridad(request):
    """
        Página para listar de Prioridad.

        Genera una instancia de los objetos de PrioridadUsuario y luego los devuleve al template listarPrioridad.html

    """
    mensaje = 'Listar Prioridad'
    messages.add_message(request, messages.INFO, mensaje)
    prioridades = PrioridadUsuario.objects.all()
    return render(request, 'usuario/listarPrioridad.html', {
        'prioridades': prioridades
    })


@login_required
@permission_required('usuarios.per_editar_prioridad')
def editarPrioridad(request, codigo):
    """
        Página para la edicion de prioridad.

        Recibe un Post con un atributo codigo de la Prioridad a editar.

        Se instancia el objeto con el identificador suministrado.

        Se alteran los datos con el Post recibido y se guardan.

    """
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


@login_required
def editarPerfilUsuario(request):
    user = User.objects.get(username=request.user)
    """
            Página para la edicion de Usuario.

            Recibe un Post con un atributo username del usuario a editar.

            Se instancian los objetos User y Usuario con el identificador suministrado.

            Se alteran los datos con el Post recibido y se guardan.

    """
    print("imprime user")
    print(user)
    if Usuario.objects.filter(usuario=user).exists():
        # print("existe detalle de usuario.")
        user_detail = Usuario.objects.get(usuario=user)
        print("en el if", user_detail, "fin if")
    else:
        # print("no existe detalle. creando uno nuevo.")
        # Superusuarios creado por línea de comando, no tienen asociado un detalle al comienzo.
        user_detail = Usuario.objects.create(usuario=user)

    if request.method == 'POST':
        # if request.user.is_superuser:
        print("post")
        user_form = EditarPerfilUser(request.POST, instance=user)
        user_detail_form = EditarPerfilUsuario(request.POST, instance=user_detail)

        if user_form.is_valid():
            # print("user form valido")
            if user_detail_form.is_valid():
                # print("formularios validos")
                user = user_form.save()  # actualiza la tabla de usuario en la bd.
                user_detail = user_detail_form.save(commit=False)  # actualiza en el model, sin guardar en BD.
                user_detail.user = user  # actualiza (por seguridad) el campo de relación.
                user_detail.save()  # actualiza detalle en la BD.
                messages.add_message(request, messages.SUCCESS,
                                     "Información del perfil de usuario -%s- se ha modificado correctamente." % user.username)
                # print("mensaje. redirigirá al home.")
                return redirect('logout')
                # else:
                #     messages.add_message(request, messages.ERROR, "Usted no tiene permisos suficientes para efectuar la operación.")
                #     return redirect('sar:home')
    else:
        print("get get get get get")
        perfil_usuario = request.user
        print(perfil_usuario)
        user_form = EditarPerfilUser(instance=request.user)
        user_detail_form = EditarPerfilUsuario(instance=user_detail)


    return render(request, 'usuario/editarPerfilUsuario.html', {
        'user_form': user_form,
        'user_detail_form': user_detail_form,
    })
