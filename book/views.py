from django.shortcuts import render, redirect
from django.urls import reverse
from django.http import HttpResponse
from .models import Author, Book
# Create your views here.
def home(request):
    books = Book.objects.all()
    return render(request, 'book/home.html', {'books':books})

def delete_book(request, pk):
    if pk:
        book = Book.objects.get(id = pk)
        book.delete()
    return redirect(reverse('book:home'))

def edit_book(request, pk):
    if request.method == 'POST':
        if pk:
            book = Book.objects.get(id = pk)
            name = request.POST.get('name')
            if name: book.name = name
            description = request.POST.get('description')
            if description: book.description = description
            author_id = request.POST.get('author_id')
            author = None
            if author_id:
                author = Author.objects.get(id = author_id)
            book.title = name
            book.description = description
            book.author = author
            book.save()
        return redirect(reverse('book:home'))
    book = Book.objects.get(id = pk)
    return render(request, 'book/edit_book.html', {'book':book})

def see_book(request, pk):
    book = Book.objects.get(id = pk)
    return render(request, 'book/see_book.html', {'book':book})

def create_book(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        description = request.POST.get('description')
        id = request.POST.get('author_id')
        if id:
            author = Author.objects.get(id = id)
        else:
            author = None
        Book.objects.create(title = name, description = description, author = author)
        return redirect(reverse('book:home'))
    authors = Author.objects.all()
    return render(request, 'book/create_book.html', {'authors': authors})