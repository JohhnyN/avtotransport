from django.urls import path
from .views import *

urlpatterns = [
    path('', AvtoListView.as_view(), name='avto')
]