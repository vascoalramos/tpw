from django.shortcuts import render, HttpResponse

from .models import *

from .forms import *


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


def book_query(request):
    if request.method == "POST":
        form = BookQueryForm(request.POST)
        if form.is_valid():
            query = form.cleaned_data["query"]
            books = Book.objects.filter(title__icontains=query)
            return render(request, "books.html", {"books": books})
    else:
        form = BookQueryForm()

    return render(request, "book-query.html", {"form": form})


def author(request, num):
    try:
        author = Author.objects.get(id=num)
        author_books = list(Book.objects.filter(authors=author))
    except Book.DoesNotExist:
        return HttpResponse("<h1>The specified book does not exist!</h1>")
    except Exception:
        return HttpResponse("<h1>Unexpected error!</h1>")
    return render(request, "author.html", {"author": author, "books": author_books})


def author_query(request, name):
    try:
        author = Author.objects.get(name=name)
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


def publisher_query(request):
    if request.method == "POST":
        try:
            publisher = Publisher.objects.get()
        except Publisher.DoesNotExist:
            return HttpResponse("<h1>The specified publisher does not exist!</h1>")
        return render(request, "publisher.html", {"publisher": publisher})

