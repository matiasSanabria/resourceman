from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^listar/$', views.listarPermisos, name='listarPermisos'),
     url(r'^agregar/$', views.agregarPermiso, name='agregarPermisos'),
     #url(r'editar/(?P<pk>\d+)$', views.editarPermiso, name='editar'),
     url(r'^editar/(?P<pk>\d+)$', views.editarPermiso, name="editarPermisos"),

     url(r'^eliminar/(?P<pk>\d+)$', views.eliminarPermiso, name="eliminarPermisos"),


]