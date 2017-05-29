
from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^listar/$', views.listarRol, name='listarRol'),
    url(r'agregar/$', views.agregarRol, name='agregarRol'),
    url(r'^editar/(?P<pk>\d+)$', views.editarRol, name="editarRol"),
    url(r'^eliminar/(?P<pk>\d+)$', views.eliminarRol, name="eliminarRol"),

]