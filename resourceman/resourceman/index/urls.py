from django.conf.urls import url
from . import views

"""
Url que redirige al index de la aplicacion
.. moduleautor = Matias Sanabria <matt31sanabria@gmail.com>
"""
urlpatterns = [

    url(r'^$', views.index, name='index')
]