from django.shortcuts import render, HttpResponse

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
    try:
        book = Book.objects.get(id=num)
    except Book.DoesNotExist:
        return HttpResponse("<h1>The specified book does not exist!</h1>")
    return render(request, "book.html", {"book": book})


def author(request, num):
    try:
        author = Author.objects.get(id=num)
        author_books = list(Book.objects.filter(authors=author))
    except Book.DoesNotExist:
        return HttpResponse("<h1>The specified book does not exist!</h1>")
    except Exception:
        return HttpResponse("<h1>Unexpected error!</h1>")
    return render(request, "author.html", {"author": author, "books": author_books})


def publisher(request, num):
    try:
        publisher = Publisher.objects.get(id=num)
    except Publisher.DoesNotExist:
        return HttpResponse("<h1>The specified publisher does not exist!</h1>")
    return render(request, "publisher.html", {"publisher": publisher})
