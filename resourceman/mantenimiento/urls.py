from django.conf.urls import url

from mantenimiento.autocomplete import MantenimientoByTipoRecursoAutocomplete
from . import views

urlpatterns = [
    url(r'^listar/$', views.listar_mantenimientos, name='listar_mantenimientos'),
    url(r'^crear/$', views.crear_mantenimiento, name='crear_mantenimiento'),
    url(r'^get_mantenimiento_recurso/', MantenimientoByTipoRecursoAutocomplete.as_view(), name='mant_by_rec-autocomplete'),
    url(r'^terminar/(?P<id>\d+)$', views.terminar_mantenimiento, name='terminar_mantenimiento'),
    url(r'^fuera_uso/(?P<id>\d+)$', views.recurso_fuera_uso, name='fuera_uso'),
]
