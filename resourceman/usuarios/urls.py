from django.conf.urls import url

from . import views

urlpatterns = [
    # ex: /permisos/
    # url(r'^$', views.listarPermisos, name='listar'),
    url(r'^listar/$', views.listarUsuario, name='listarUsuario'),
    # url(r'^listar/(?P<pk>\d+)$',), views
    # ex: /permisos/agregar/
    url(r'^agregar/$', views.crearUsuario, name='agregarUsuario'),

    # ex: /permisos/editar/
    # url(r'editar/(?P<pk>\d+)$', views.editarPermiso, name='editar'),
    url(r'^editar/(?P<username>\w+)$', views.editarUsuario, name="editarUsuario"),
    #
    url(r'^eliminar/(?P<username>\w+)$', views.eliminarUsuario, name="eliminarUsuario"),

    url(r'^agregarPrioridad/$', views.agregarPrioridad, name='agregarPrioridad'),

    url(r'^listarPrioridad/$', views.listarPrioridad, name='listarPrioridad'),

    url(r'^editarPrioridad/(?P<codigo>\w+)$', views.editarPrioridad, name='editarPrioridad'),

]