from django.contrib import admin
from django.urls import path, include
from . import views
app_name = 'book'
urlpatterns = [
    path('', views.home, name='home'),
    path('delete_book/<int:pk>', views.delete_book, name='delete_book'),
    path('edit_book/<int:id>', views.edit_book, name='edit_book'),
    path('see_book/<int:id>', views.see_book, name='see_book'),
]