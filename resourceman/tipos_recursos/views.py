from django.contrib.auth.decorators import login_required, permission_required
from django.shortcuts import redirect, render

from reservas.models import Reservas
from .models import CaracteristicasRecursos
from .forms import TipoRecursoForm, EstadoForm, RecursoForm, EncargadoForm
from .models import TipoRecurso, Estados, Recurso, Encargado
from mantenimiento.models import Mantenimiento
from django.contrib import messages
from rest_framework.decorators import api_view
from rest_framework.response import Response

__author__ = 'matt'

@login_required
@permission_required('tipos_recursos.per_crear_tiporecurso')
def crear(request):
    """
    Permite crear un nuevo tipo de recurso con los siguientes datos
    
    nombre nombre: del tipo de recurso que se utiliza como clave primaria
    descripcion: descripcion del tipo de recurso
    lista de caracteristicas: lista de las caracteristicas que seran utilizadas para instanciar una clase de recurso
    estado: indica si el tipo de recurso esta activo o no
    - A 'Activo'
    - I 'Inactivo'
    :param request: 
    :return: el formulario para crear otro tipo de recurso
    """
    if request.method == "POST":

        tipo_recursoform = TipoRecursoForm(request.POST)
        encargadoform = EncargadoForm(request.POST)
        if tipo_recursoform.is_valid():
            if encargadoform.is_valid():
                tipo = tipo_recursoform.save(commit=False)
                tipo.save()
                encar = encargadoform.save(commit=False)
                encar.tipo_recurso = tipo
                encar.save()
                return redirect('crear')

            else:
                pass
        else:
            pass
    tipo_recurso = TipoRecursoForm()
    encargado = EncargadoForm()
    return render(request, 'tipo_recurso/crear_tipos_recursos.html', {
        'tipo_recurso': tipo_recurso, 'encargado': encargado})


@login_required
@permission_required('tipos_recursos.per_editar_tiporecurso')
def editar(request, nombre):
    """
    Permite editar tipo de recurso con los siguientes datos

    nombre nombre: del tipo de recurso que se utiliza como clave primaria
    descripcion: descripcion del tipo de recurso
    lista de caracteristicas:  lista de las caracteristicas que seran utilizadas para instanciar una clase de recurso
    estado: indica si el tipo de recurso esta activo o no
    - A 'Activo'
    - I 'Inactivo'
    encargado: referencia a un usuario con permisos para manejar recursos
    :param request: 
    :return: el formulario para editar otro tipo de recurso
    """
    mensaje = 'Modificar Tipo de Recurso'
    messages.add_message(request, messages.INFO, mensaje)
    editar = TipoRecurso.objects.get(nombre=nombre)
    encargado = Encargado.objects.get(tipo_recurso=nombre)
    if request.method == 'POST':
        editar_form = TipoRecursoForm(request.POST, instance=editar)
        encargado_form = EncargadoForm(request.POST, instance=encargado)
        if editar_form.is_valid():
            if encargado_form.is_valid():
                editar_form.save()
                encargado_form.save()
                return redirect('listar')

        return render(request, 'tipo_recurso/editar_tipo_recurso.html', {
            'editar_form': editar_form,
            'encargado_form': encargado_form,
            'nombre': nombre
        })
    else:
        editar_form = TipoRecursoForm(instance=editar)
        encargado_form = EncargadoForm(instance=encargado)
        return render(request, 'tipo_recurso/editar_tipo_recurso.html', {
            'editar_form': editar_form,
            'encargado_form': encargado_form,
            'nombre': nombre
        })


@login_required
@permission_required('tipos_recursos.per_eliminar_tiporecurso')
def eliminar(request, nombre):
    """
    Permite eliminar tipo de recurso con los siguientes datos
    
    nombre nombre: del tipo de recurso que se utiliza como clave primaria
    :param request: 
    :return: el formulario para listar los tipos de recursos
    """

    eliminar = TipoRecurso.objects.get(nombre=nombre)
    mensaje = "Tipo de Recurso \'%s\' eliminado..\n" % eliminar
    messages.add_message(request, messages.INFO, mensaje)
    eliminar.estado = 'I'
    eliminar.save()
    return redirect('../listar')


@api_view(['GET'])
def get_tipo_recurso(request, id):
    """
    Metodo rest que permite obtener las caracteristicas de un tipo de recurso
    para ser mostrado en el formulario de creacion de un recurso.
    :param request: 
    :param id: es el identificador del tipo de recurso seleccionado
    :return: una lista de las caracteristicas del tipo de recurso
    """
    caracteristicas = TipoRecurso.objects.get(nombre=id)
    print(caracteristicas.lista_caracteristicas)
    return Response({'[' + caracteristicas.lista_caracteristicas + ']'})


@login_required
@permission_required('tipos_recursos.per_listar_tiporecurso')
def listar_tipos_recursos(request):
    """
    Permite listar los tipos de recursos con los siguientes datos

    nombre nombre: del tipo de recurso que se utiliza como clave primaria
    descripcion: descripcion del tipo de recurso
    lista de caracteristicas:  lista de las caracteristicas que seran utilizadas para instanciar una clase de recurso
    estado: indica si el tipo de recurso esta activo o no
    - A 'Activo'
    - I 'Inactivo'
    :param request: 
    :return: el formulario para listar los tipos de recursos
    """
    mensaje = 'Listar Permisos'
    messages.add_message(request, messages.INFO, mensaje)
    lista = TipoRecurso.objects.all()
    return render(request, 'tipo_recurso/listar_tipos_recursos.html', {'lista': lista})


########################################################################################################################
@login_required
@permission_required('tipos_recursos.per_listar_estados')
def listar_estados(request):
    """
    Permite listar los estados de los recursos con los siguientes datos

    codigo: del estado del recurso que se utiliza como clave primaria
    descripcion: descripcion del estado del recurso
    
    :param request: 
    :return: el formulario para listar los estados de los recursos
    """
    mensaje = 'Listar Estados'
    messages.add_message(request, messages.INFO, mensaje)
    lista = Estados.objects.all()
    return render(request, 'estados/listar_estados.html', {'lista': lista})


@login_required
@permission_required('tipos_recursos.per_crear_estado')
def crear_estado(request):
    """
    Permite crear un estado de recurso con los siguientes datos
    codigo: del estado de recurso que se utiliza como clave primaria
    descripcion: descripcion del estado de recurso
    :param request: 
    :return: el formulario para crear otro tipo de recurso
    """
    if request.method == "POST":
        estado = EstadoForm(request.POST)
        if estado is not None:
            if estado.is_valid():
                estado.save()
                messages.success(request, "Estado guardado correctamente")
                return redirect('crear_estado')
        else:
            messages.error(request, "Ocurrio un error al guardar el estado. Vuelva a intentarlo")

    estado = EstadoForm()
    return render(request, 'estados/crear_estado.html', {'estado': estado})


@login_required
@permission_required('tipos_recursos.per_editar_estado')
def editar_estado(request, codigo):
    """
    Permite editar un estado de recurso con los siguientes datos
    codigo:  del estado de recurso que se utiliza como clave primaria
    descripcion: descripcion del estado de recurso
    :param request: 
    :return: el formulario para editar otro tipo de recurso
    """
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
@permission_required('tipos_recursos.per_eliminar_estado')
def eliminar_estado(request, codigo):
    """
    Permite eliminar estado de recurso

    nombre nombre: del estado de recurso a eliminar
    :param request: 
    :return: el formulario para listar los estados de recursos
    """
    eliminar = Estados.objects.get(codigo=codigo)
    mensaje = "Estado de Recurso \'%s\' eliminado..\n" % eliminar
    messages.add_message(request, messages.INFO, mensaje)
    eliminar.codigo = 'I'
    return redirect('../listar_estados')

########################################################################################################################

@login_required
@api_view(['GET', 'POST'])
@permission_required('tipos_recursos.per_crear_recurso')
def crear_recurso(request):
    """
    Crea un nuevo recurso con los siguientes datos
    
    codigo_recurso: codigo del recurso utilizado como clave primaria
    nombre_recurso: nombre para el recurso
    descripcion_recurso: descripcion del recurso a crear
    tipo_recurso: indica a que tipo de recurso pertenece
    activo: indica si esta activo o inactivo
    :param request: 
    :return: formulario para crear un nuevo recurso
    """
    if request.method == "POST":
        recurso = RecursoForm(request.POST)
        if recurso.is_valid():
            recurso.save()
            return redirect('crear_recurso')
        else:
            pass

    recurso = RecursoForm()
    caracteristicas = CaracteristicasRecursos()
    return render(request, 'recurso/crear_recurso.html', {'recurso': recurso, 'caracteristicas': caracteristicas})


@login_required
@permission_required('tipos_recursos.per_editar_recurso')
def editar_recurso(request, codigo_recurso):
    """
    Edita recurso con los siguientes datos

    codigo_recurso: codigo del recurso utilizado como clave primaria
    nombre_recurso: nombre para el recurso
    descripcion_recurso: descripcion del recurso a crear
    tipo_recurso: indica a que tipo de recurso pertenece
    activo: indica si esta activo o inactivo
    :param request: 
    :return: formulario para listar los recursos
    """
    mensaje = 'Modificar Recurso'
    messages.add_message(request, messages.INFO, mensaje)
    editar = Recurso.objects.get(codigo_recurso=codigo_recurso)

    if request.method == 'POST':
        editar_form = RecursoForm(request.POST, instance=editar)
        if editar_form.is_valid():
            editar_form.save()
            return redirect('listar_recursos')
        else:
            editar_form = RecursoForm(request.POST, instance=editar)

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
@permission_required('tipos_recursos.per_eliminar_recurso')
def eliminar_recurso(request, codigo_recurso):
    """
    Elimina un recurso
    :param request: 
    :param codigo: del recurso a ser eliminado
    :return: lista de todos los recursos disponibles
    """
    eliminar = Recurso.objects.get(codigo_recurso=codigo_recurso)
    mensaje = "Recurso \'%s\' eliminado..\n" % eliminar
    messages.add_message(request, messages.INFO, mensaje)
    eliminar.estado = Estados.objects.get(codigo="FUS")
    eliminar.activo = 'I'
    eliminar.save()
    return redirect('../listar_recursos')


@login_required
@permission_required('tipos_recursos.per_listar_recursos')
def listar_recursos(request):
    """
    Lista todos los recursos disponibles en el sistema
    :param request: 
    :return: 
    """
    mensaje = 'Listar Recursos'
    messages.add_message(request, messages.INFO, mensaje)
    lista = Recurso.objects.all()
    return render(request, 'recurso/listar_recursos.html', {'lista': lista})


@login_required
def listar_encargado(request):
    """
    Lista todos los encargados de tipo de recursos disponibles en el sistema
    :param request:
    :return:
    """
    mensaje = 'Listar Encargados'
    messages.add_message(request, messages.INFO, mensaje)
    lista = Encargado.objects.all()
    return render(request, 'tipo_recurso/listar_encargados.html', {'lista': lista})

@login_required
@permission_required('tipos_recursos.per_historial_mantenimiento_recursos')
def historial_mantenimientos(request, codigo_recurso):
    """
    Muestra la lista de mantenimientos en curso del sistema
    :param request:
    :return:
    """
    item = Recurso.objects.get(codigo_recurso=codigo_recurso)
    mensaje = 'Historial Mantenimientos'
    messages.add_message(request, messages.INFO, mensaje)
    mantenimientos = Mantenimiento.objects.filter(recurso_id=item)
    return render(request, 'recurso/historial_mantenimientos.html', {'mantenimientos': mantenimientos,})

@login_required
@permission_required('tipos_recursos.per_listar_reservas')
def historial_reservas(request):
    """
    Muestra la lista de reservas Terminadas y Canceladas del sistema
    :param request:
    :return:
    """
    mensaje = 'Historial de Reservas'
    messages.add_message(request, messages.INFO, mensaje)
    reservas = Reservas.objects.all().filter(tipo_recurso__encargado__usuario=request.user)
    return render(request, 'reservas/historial_reservas_admin.html', {'reservas': reservas})