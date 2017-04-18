from django.shortcuts import render
from permisos.models import AuthPermission
# Create your views here.
from django.http import HttpResponse
from django.template import RequestContext,loader
from django.shortcuts import render_to_response

def listarPermisos(request):
    #template = loader.get_template('templates/index.html')
    #return HttpResponse("Listar permisos")#template.render())
    #permisos_list = AuthPermission.objects.all()
    #context = {'object_list': permisos_list}
    #return render(request, 'permisos/index.html', context)
    return HttpResponse("Listar permisos")

def editarPermiso(request):
    return render_to_response("editarPermisos.html")


def agregarPermiso(request):
    return HttpResponse("Agregar permisos")
