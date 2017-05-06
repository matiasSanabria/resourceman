from django.conf.urls import url
from . import views

urlpatterns = [
    ###################################################################################################################
    # Url de los tipos de recursos
    ###################################################################################################################
    url(r'^listar/$', views.listar_tipos_recursos, name='listar'),
    url(r'^crear/$', views.crear, name='crear'),
    url(r'^editar/(?P<nombre>\w+)$', views.editar, name='editar'),
    url(r'^eliminar/(?P<nombre>\w+)$', views.eliminar, name='eliminar'),

    ###################################################################################################################
    # Url de los estados
    ###################################################################################################################
    url(r'^listar_estados/$', views.listar_estados, name='listar_estados'),
    url(r'^crear_estado/$', views.crear_estado, name='crear_estado'),
    url(r'^editar_estado/(?P<codigo>\w+)$', views.editar_estado, name='editar_estado'),
    url(r'^eliminar_estado/(?P<codigo>\w+)$', views.eliminar_estado, name='eliminar_estado'),

    ###################################################################################################################
    # Url de los recursos
    ###################################################################################################################
    url(r'^listar_recursos/$', views.listar_recursos, name='listar_recurso'),
    url(r'^crear_recurso/$', views.crear_recurso, name='crear_recurso'),
    url(r'^crear_recurso/get_tipo_recurso/(?P<id>\w+)$', views.get_tipo_recurso, name='get_tipo_recurso'),
    url(r'^editar_recurso/(?P<codigo_recurso>\w+)$', views.editar_recurso, name='editar_recurso'),

    #url(r'^eliminar_recurso/(?P<codigo_recurso>\w+)$', views.eliminar_recurso, name='eliminar_recurso'),

]