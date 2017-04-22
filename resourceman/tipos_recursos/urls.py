from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^listar/$', views.listar_tipos_recursos, name='listar'),
    url(r'^crear/$', views.crear, name='crear'),
    url(r'^editar/(?P<nombre>\w+)$', views.editar, name='editar'),
    url(r'^eliminar/(?P<nombre>\w+)$', views.eliminar, name='eliminar'),

    ##################################################################
    url(r'^listar_estados/$', views.listar_estados, name='listar_estados'),
    url(r'^crear_estado/$', views.crear_estado, name='crear_estado'),
    url(r'^editar_estado/(?P<codigo>\w+)$', views.editar_estado, name='editar_estado'),
    url(r'^eliminar_estado/(?P<codigo>\w+)$', views.eliminar_estado, name='eliminar_estado'),
]