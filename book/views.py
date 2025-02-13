from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Author, Book
# Create your views here.
def home(request):
    books = Book.objects.all()
    return render(request, 'book/home.html', {'books':books})

def delete_book(request, pk):
    book = Book.objects.get(id = pk)
    book.delete()
    return redirect(request, 'book:home')

def edit_book(request, pk):
    if request.method == 'POST':
        book = Book.objects.get(id = pk)
        name = request.POST.get('name')
        if name: book.name = name
        description = request.POST.get('description')
        if description: book.description = description
        author_id = request.POST.get('author_id')
        author = Author.objects.get(id = author_id)
        authors = Author.objects.all()
    book = Book.objects.get(id = pk)
    return render(request, 'book/edit_book.html', {'books':book})

def see_book(request, pk):
    books = Book.objects.all()
    return render(request, 'book/home.html', {'books':books})

def create_book(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        description = request.POST.get('description')
        author_id = request.POST.get('author_id')
        author = Author.objects.get(id = author_id)
        Book.objects.create(name = name, description = description, author = author)
        return redirect(request, 'book:home')
    return render(request, 'book/create_book.html')