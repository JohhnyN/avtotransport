from django.template.defaulttags import url
from django.urls import path, re_path
from django.contrib.auth import views as auth_views

from . import views
from .views import *

urlpatterns = [
    path('', AutomobileListView.as_view(), name='avto'),
    path('create/', views.create, name='create'),
    path('login/', LoginUser.as_view(), name='login'),
    path('logout/', logout_user, name='logout'),
    path('change-password/', views.UpdatePassword.as_view(), name="update_password"),
    path('password-change-done/', views.password_change_done, name="password_change_done"),
    # path('change-password/', auth_views.PasswordChangeView.as_view(
    #         template_name='avto/password_change_done.html',
    #         success_url='/'
    #     ),
    #     name='change_password'
    # ),
]


