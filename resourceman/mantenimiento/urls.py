from django.conf.urls import url

from mantenimiento.autocomplete import MantenimientoByTipoRecursoAutocomplete
from . import views

urlpatterns = [
    url(r'^listar/$', views.listar_mantenimientos, name='listar_mantenimientos'),
    url(r'^crear/$', views.crear_mantenimiento, name='crear_mantenimiento'),
    url(r'^get_mantenimiento_recurso/', MantenimientoByTipoRecursoAutocomplete.as_view(), name='mant_by_rec-autocomplete'),
    url(r'^terminar/(?P<id>\d+)$', views.terminar_mantenimiento, name='terminar_mantenimiento'),
    url(r'^fuera_uso/(?P<id>\d+)$', views.recurso_fuera_uso, name='fuera_uso'),
    url(r'^listar/preventivo/$', views.listarMantenimientoProgramado, name='listar_mantenimientos_programados'),
    url(r'^menu/$', views.submenu_mantenimientos, name='mantenimientos'),
    url(r'^crear/programado(?P<pk>\w+)$', views.crear_mantenimiento_preventivo, name='crear_mantenimiento_preventivo'),
    url(r'^posponer/(?P<pk>\w+)$', views.posponer_preventivo, name='posponer'),

]
