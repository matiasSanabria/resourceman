from django.conf.urls import url
from . import views

urlpatterns = [
    ###################################################################################################################
    # Url de Reservas
    ###################################################################################################################
    url(r'^$',views.listarReserva, name='lisatar_reserva'),
    url(r'^listar/user/$', views.listarReservasUser, name='listar_reservas_usuarios'),
    url(r'^listar/admin/$', views.listarReservasAdmin, name='listar_reservas_admin'),
    url(r'^crear/$', views.crearReserva, name='crear_reserva'),
    # url(r'^editar/(?P<nombre>\w+)$', views.editar, name='editar'),
    # url(r'^eliminar/(?P<nombre>\w+)$', views.eliminar, name='eliminar'),
]