from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
from django.template import RequestContext,loader


def index(request):
    #template = loader.get_template('templates/index.html')
    return HttpResponse("Listar permisos")#template.render())


def editarPermiso(request):
    return HttpResponse("Editar permisos")


def agregarPermiso(request):
    return HttpResponse("Agregar permisos")
