__author__ = 'josegregorio'

from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^login$', views.LoginView.as_view()), #
    url(r'^register', views.register, name='register'),
    url(r'^logout', views.logout, name='logout'),
    url(r'^reset_password', views.logout, name='password_reset'),
]