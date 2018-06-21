from django.contrib import admin
from django.urls import path,re_path
from .import views

app_name = 'accounts'

urlpatterns =[
    re_path(r'^registration/$', views.registration_view, name="registration"),
    re_path(r'^registration/authorization/$', views.authorization_view, name="authorization")
]