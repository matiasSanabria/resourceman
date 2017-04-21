from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'listar/$', views.listar_tipos_recursos, name='listar_tipos_recursos'),
    url(r'crear/$', views.crear, name='crear_tipo_recurso'),
    url(r'editar/(?P<nombre>\d+)$', views.editar, name='editar_tipo_recurso'),
    url(r'eliminar/(?P<nombre>\d+)$', views.eliminar, name='eliminar_tipo_recurso'),
]