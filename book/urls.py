from django.contrib import admin
from django.urls import path, include
from . import views
app_name = 'book'
urlpatterns = [
    path('', views.home, name='home')
]