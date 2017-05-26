from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^listar/$', views.listarUsuario, name='listarUsuario'),
    url(r'^agregar/$', views.crearUsuario, name='agregarUsuario'),
    url(r'^editar/(?P<username>\w+)$', views.editarUsuario, name="editarUsuario"),
    url(r'^eliminar/(?P<username>\w+)$', views.eliminarUsuario, name="eliminarUsuario"),
    url(r'^agregarPrioridad/$', views.agregarPrioridad, name='agregarPrioridad'),
    url(r'^listarPrioridad/$', views.listarPrioridad, name='listarPrioridad'),
    url(r'^editarPrioridad/(?P<codigo>\w+)$', views.editarPrioridad, name='editarPrioridad'),
    url(r'^bajarPrioridad/(?P<codigo>\w+)$', views.bajarPrioridad, name='bajarPrioridad'),
    url(r'^subirPrioridad/(?P<codigo>\w+)$', views.subirPrioridad, name='subirPrioridad'),
    url(r'^editarPerfilUsuario/$', views.editarPerfilUsuario, name='editarPerfilUsuario'),
]