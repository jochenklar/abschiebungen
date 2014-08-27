from django.conf.urls import patterns, include, url
from rest_framework import routers
from django.contrib import admin
from data import views


router = routers.DefaultRouter()
#router.register(r'absLandNatio', views.AbsLandNatioViewSet)


urlpatterns = patterns('',
    url(r'^', include(router.urls)),
    url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework'))
)

#urlpatterns = patterns('',
#    url(r'^$', 'abschiebungen.views.home', name='home'),
#)
