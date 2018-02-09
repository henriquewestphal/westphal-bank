from django.conf.urls import include, url
from django.contrib import admin
from usuarios.views import RegistrarUsuarioView
from usuarios import views
from django.contrib.auth import views as auth_views

urlpatterns = [
    url(r'^registrar/$', RegistrarUsuarioView.as_view(), name='registrar'),
    url(r'^login/$', auth_views.login, {'template_name':'login.html'}, name='login'),
    url(r'^logout/$', auth_views.logout_then_login, {'login_url':'/login/'}, name='logout'),
]
