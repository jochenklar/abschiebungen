from django.conf.urls import patterns, include, url
from data import urls
from django.contrib import admin

admin.autodiscover()

urlpatterns = patterns('',
    url(r'^$', 'abschiebungen.views.home', name='home'),
    url(r'^api/', include(urls)),
    url(r'^admin/', include(admin.site.urls)),
)
