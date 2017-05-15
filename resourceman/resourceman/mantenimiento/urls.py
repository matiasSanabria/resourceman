from django.conf.urls import url

from . import views

urlpatterns = [
    # url(r'^listar/$', views.listar, name='listar_mantenimientos'),
    url(r'^crear/$', views.crear_mantenimiento, name='crear_mantenimiento'),
]