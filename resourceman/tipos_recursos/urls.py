from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'listar/$', views.listar_tipos_recursos, name='listar'),
    url(r'crear/$', views.crear, name='crear'),
    url(r'editar/(?P<nombre>\w+)$', views.editar, name='editar'),
    url(r'eliminar/(?P<nombre>\w+)$', views.eliminar, name='eliminar'),

    ##################################################################
    url(r'listar/$', views.listar_estados, name='listar'),
]