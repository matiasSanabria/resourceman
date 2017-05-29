from django.conf.urls import url

from . import views

urlpatterns = [

    url(r'^menu/$', views.submenu_configuraciones, name='configuraciones'),
    url(r'^registro_usuario/(?P<id>\d+)$', views.registro_usuario, name='registro_usuario'),
]