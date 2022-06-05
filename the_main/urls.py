from django.contrib import admin
from django.urls import path
from . import views

urlpatterns=[
    path('', views.personal_info, name='main_page')
]