from django.conf.urls import url
from django.conf.urls import include
from rest_framework.routers import DefaultRouter

from . import views

router = DefaultRouter()
router.register('poi', views.Poi, basename='poi')

urlpatterns = [
    url(r'', include(router.urls)),
    url(r'^djmapsap/', views.PoiAP.as_view()),
]
