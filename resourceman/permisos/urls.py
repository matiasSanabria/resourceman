from django.conf.urls import url

from . import views

urlpatterns = [
    # ex: /permisos/
    # url(r'^$', views.listarPermisos, name='listar'),
    url(r'^listar/$', views.listarPermisos, name='listar'),
    # url(r'^listar/(?P<pk>\d+)$',), views
    # ex: /permisos/agregar/
    url(r'agregar/$', views.agregarPermiso, name='agregar'),
    # ex: /permisos/editar/
    # url(r'editar/(?P<pk>\d+)$', views.editarPermiso, name='editar'),
    url(r'^editar/(?P<pk>\d+)$', views.editarPermiso, name="editar"),

    url(r'^eliminar/(?P<pk>\d+)$', views.eliminarPermiso, name="eliminar"),


]