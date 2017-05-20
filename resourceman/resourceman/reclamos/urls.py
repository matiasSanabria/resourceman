from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^listar/$', views.list_reclamo, name='listarReclamos'),
    url(r'^crear/$', views.crear_reclamo, name='crearReclamo'),
    url(r'^ver/(?P<pk>\d+)$', views.ver_reclamo, name="verReclamo"),
    url(r'^editar/(?P<pk>\d+)$', views.editar_reclamo, name="editarReclamo"),
]