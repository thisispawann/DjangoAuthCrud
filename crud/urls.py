from django.contrib import admin
from django.urls import path

from . import views

# Creating URLs

urlpatterns = [
    path('', views.index, name='index')
]
