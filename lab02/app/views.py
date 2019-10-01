from django.shortcuts import render

from .models import *


# Create your views here.
def books(request):
    books_list = Book.objects.all()
    return render(request, "books.html", {"books": books_list})


def authors(request):
    authors_list = Author.objects.all()
    return render(request, "authors.html", {"authors": authors_list})


def publishers(request):
    publishers_list = Publisher.objects.all()
    return render(request, "publishers.html", {"books": publishers_list})


def book(request, num):
    return render(request, "book.html", {"book": Book.objects.get(id=num)})


def author(request, num):
    author_books = list(Book.objects.filter(authors=Author.objects.get(id=num)))
    return render(request, "author.html", {"author": Author.objects.get(id=num), "books": author_books})


def publisher(request, num):
    return render(request, "publisher.html", {"publisher": Publisher.objects.get(id=num)})
