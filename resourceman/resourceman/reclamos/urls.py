import django.conf.urls
from . import views

urlpatterns = [
    # ex: /permisos/
    # url(r'^$', views.listarPermisos, name='listar'),
    django.conf.urls.url(r'^listar/$', views.list_reclamo, name='listarReclamos'),
    # url(r'^listar/(?P<pk>\d+)$',), views
    # ex: /permisos/agregar/
    django.conf.urls.url(r'^crear/$', views.crear_reclamo, name='crearReclamo'),
    # ex: /permisos/editar/
    # url(r'editar/(?P<pk>\d+)$', views.editarPermiso, name='editar'),
    django.conf.urls.url(r'^ver/(?P<pk>\d+)$', views.ver_reclamo, name="verReclamo"),
    django.conf.urls.url(r'^editar/(?P<pk>\d+)$', views.editar_reclamo, name="editarReclamo"),
]