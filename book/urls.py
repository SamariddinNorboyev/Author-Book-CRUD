from django.contrib import admin
from django.urls import path, include
from . import views
app_name = 'book'
urlpatterns = [
    path('', views.home, name='home'),
    path('create-book/', views.create_book, name='create-book'),
    path('delete_book/<int:pk>', views.delete_book, name='delete_book'),
    path('edit_book/<int:pk>', views.edit_book, name='edit_book'),
    path('see_book/<int:pk>', views.see_book, name='see_book'),



    path('authors/', views.authors, name='authors'),
    path('create-author/', views.create_author, name='create-author'),
    path('delete_author/<int:pk>', views.delete_author, name='delete_author'),
    path('edit_author/<int:pk>', views.edit_author, name='edit_author'),
    path('see_author/<int:pk>', views.see_author, name='see_author'),
]