from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    # ex: /permisos/agregar/
    url(r'agregar/$', views.agregarPermiso, name='agregar'),
    # ex: /permisos/editar/
    url(r'editar/$', views.editarPermiso, name='editar'),
]