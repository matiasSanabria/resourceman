from django.conf.urls import url

from ..reservas.autocomplete import RecursoByTipoRecursoAutocomplete
from . import views

urlpatterns = [
    ###################################################################################################################
    # Url de Reservas
    ###################################################################################################################
    url(r'^$', views.listarReserva, name='lisatar_reserva'),
    url(r'^listar/user/$', views.listarReservasUser, name='listar_reservas_usuarios'),
    url(r'^listar/admin/$', views.listarReservasAdmin, name='listar_reservas_admin'),
    url(r'^crear/$', views.crearReserva, name='crear_reserva'),
    url(r'^get_recurso_by_tipo', RecursoByTipoRecursoAutocomplete.as_view(), name='recu_by_tipo-autocomplete'),
    url(r'^enCurso/(?P<pk>\d+)$', views.enCurso, name='enCurso'),
    url(r'^devuelto/(?P<pk>\d+)$', views.devuelto, name='devuelto'),
    url(r'^nodevuelto/(?P<pk>\d+)$', views.noDevuelto, name='noDevuelto'),
    url(r'^cancelado/(?P<pk>\d+)$', views.cancelado, name='cancelado'),
    # url(r'^editar/(?P<nombre>\w+)$', views.editar, name='editar'),
    # url(r'^eliminar/(?P<nombre>\w+)$', views.eliminar, name='eliminar'),
]
