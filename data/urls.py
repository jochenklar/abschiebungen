from django.conf.urls import patterns, include, url
from rest_framework import routers
from data import views

router = routers.DefaultRouter()
router.register(r'AbschiebungBundeslaender', views.AbschiebungBundeslaender)

urlpatterns = patterns('',
    url(r'^', include(router.urls)),
)
