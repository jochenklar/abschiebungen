from django.conf.urls import patterns, include, url
from data import urls

urlpatterns = patterns('',
    url(r'^$', 'abschiebungen.views.home', name='home'),
    url(r'^api/', include(urls)),
)
