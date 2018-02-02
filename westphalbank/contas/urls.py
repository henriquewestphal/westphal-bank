from django.conf.urls import include, url
from django.contrib import admin
from contas import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^contas/(?P<conta_id>\d+)$', views.exibir, name='exibir'),
]
