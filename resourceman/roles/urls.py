from django.conf.urls import url

from . import views

urlpatterns = [
    # ex: /roles/listar
    url(r'^listar/$', views.listarRol, name='listarRol'),
    # ex: /roles/agregar/
    url(r'agregar/$', views.agregarRol, name='agregarRol'),
    # ex: /roles/editar/
    url(r'^editar/(?P<pk>\d+)$', views.editarRol, name="editarRol"),
    # # ex: /roles/eliminar/
    url(r'^eliminar/(?P<pk>\d+)$', views.eliminarRol, name="eliminarRol"),

]