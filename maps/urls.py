from django.urls import path
from django.conf.urls import url
from . import views

urlpattern = [
    url(r'', views.default_map, name="default"),
]
