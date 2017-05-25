"""resourceman URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.10/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url, include
from django.contrib import admin
from django.contrib.auth.views import password_reset, password_reset_done, password_reset_confirm, \
    password_reset_complete

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^accounts/', include('login.urls')),
    url(r'', include('index.urls')),
    url(r'^permisos/', include('permisos.urls')),
    url(r'^roles/', include('roles.urls')),
    url(r'^usuarios/', include('usuarios.urls')),
    url(r'^configuraciones/', include('configuraciones.urls')),
    url(r'^tipo_recurso/', include('tipos_recursos.urls')),
    url(r'^recursos/', include('tipos_recursos.urls')),
    url(r'^estados/', include('tipos_recursos.urls')),
    url(r'^reclamos/', include('reclamos.urls')),
    url(r'^mantenimientos/', include('mantenimiento.urls')),
    url(r'^reservas/', include('reservas.urls')),
    url(r'^reset/password_reset', password_reset, {'template_name': 'registration/password_reset_form.html',
                                                   'email_template_name': 'registration/password_reset_email.html'},
        name='password_reset'),
    url(r'^password_reset_done', password_reset_done, {'template_name': 'registration/password_reset_done.html'},
        name='password_reset_done'),
    url(r'^reset/(?P<uidb64>[0-9A-Za-z_\-]+)/(?P<token>.+)/$', password_reset_confirm,
        {'template_name': 'registration/password_reset_confirm.html'},
        name='password_reset_confirm'),
    url(r'^reset/done', password_reset_complete, {'template_name': 'registration/password_reset_complete.html'},
        name='password_reset_complete'),

]
