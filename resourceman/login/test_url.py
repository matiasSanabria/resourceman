from django.conf.urls import include
from django.contrib import admin
from patterns import patterns

admin.autodiscover()

urlpatterns = patterns('',
    (r'^accounts/', include('login.urls')),
    (r'^admin/', include(admin.site.urls)),
)