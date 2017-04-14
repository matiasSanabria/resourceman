from django.conf.urls import url

from . import views

urlpatterns = [
    # ex: /permisos/
    url(r'^$', views.listarPermisos, name='listar'),
    # ex: /permisos/agregar/
    url(r'agregar/$', views.agregarPermiso, name='agregar'),
    # ex: /permisos/editar/
    url(r'editar/$', views.editarPermiso, name='editar'),
]