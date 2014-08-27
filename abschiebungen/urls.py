from django.conf.urls import patterns, include, url

urlpatterns = patterns('',
    url(r'^$', 'abschiebungen.views.home', name='home'),
)
