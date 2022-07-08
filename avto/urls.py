from django.template.defaulttags import url
from django.urls import path, re_path

from . import views
from .views import *

urlpatterns = [
    path('', AutomobileListView.as_view(), name='avto'),
    path('create/', views.create, name='create'),
    re_path(r'^/get_car_models/$', views.get_car_models),
]