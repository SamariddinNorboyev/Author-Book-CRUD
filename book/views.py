from django.shortcuts import render, redirect
from django.urls import reverse
from django.http import HttpResponse
from .models import Author, Book
from datetime import datetime
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
    authors = Author.objects.all()
    book = Book.objects.get(id = pk)
    return render(request, 'book/edit_book.html', {'book':book, 'authors': authors})

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





def authors(request):
    authors = Author.objects.all()
    books = Book.objects.all()
    return render(request, 'book/authors.html', {'authors':authors, 'books':books})
def delete_author(request, pk):
    if pk:
        author = Author.objects.get(id = pk)
        author.delete()
    return redirect(reverse('book:authors'))

def edit_author(request, pk):
    if request.method == 'POST':
        if pk:
            author = Author.objects.get(id = pk)
            name = request.POST.get('name')
            if name: author.name = name
            surname = request.POST.get('surname')
            if surname: author.surname = surname
            birthday = request.POST.get('birthday')
            birthday = datetime.strptime(birthday, "%Y-%m-%dT%H:%M").strftime("%Y-%m-%d")
            author.name = name
            author.surname = surname
            author.birthday = birthday
            author.save()
        return redirect(reverse('book:authors'))
    author = Author.objects.get(id = pk)
    author.birthday = author.birthday.strftime("%Y-%m-%dT%H:%M")
    return render(request, 'book/edit_author.html', {'author':author})

def see_author(request, pk):
    books = Book.objects.all()
    author = Author.objects.get(id = pk)
    return render(request, 'book/see_author.html', {'author':author, 'books':books})

def create_author(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        surname = request.POST.get('surname')
        birthday = request.POST.get('birthday')
        birthday = datetime.strptime(birthday, "%Y-%m-%dT%H:%M").strftime("%Y-%m-%d")
        Author.objects.create(name = name, surname = surname, birthday = birthday)
        return redirect(reverse('book:authors'))
    return render(request, 'book/create_author.html')