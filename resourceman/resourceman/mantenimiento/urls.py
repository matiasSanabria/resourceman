from django.conf.urls import url

from ..mantenimiento.autocomplete import MantenimientoByTipoRecursoAutocomplete
from . import views

urlpatterns = [
    # url(r'^listar/$', views.listar, name='listar_mantenimientos'),
    url(r'^crear/$', views.crear_mantenimiento, name='crear_mantenimiento'),
    url(r'^get_mantenimiento_recurso/', MantenimientoByTipoRecursoAutocomplete.as_view(), name='mant_by_rec-autocomplete'),
]