from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^listar/$', views.list_reclamo, name='listarReclamos'),
    url(r'^crear/$', views.crear_reclamo, name='crearReclamo'),
    url(r'^ver/(?P<pk>\d+)$', views.ver_reclamo, name="verReclamo"),
    url(r'^editar/(?P<pk>\d+)$', views.editar_reclamo, name="editarReclamo"),
    url(r'^listar_estados/$', views.listar_estados_reclamos, name='listar_estados_reclamos'),
    url(r'^crear_estado/$', views.crear_estado_reclamo, name='crear_estado_reclamo'),
    url(r'^editar_estado/(?P<codigo>\w+)$', views.editar_estado_reclamo, name="editar_estado_reclamo"),
    url(r'^eliminar_estado/(?P<codigo>\w+)$', views.eliminar_estado_reclamo, name="eliminar_estado_reclamo"),
]