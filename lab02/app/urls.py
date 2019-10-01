from django.urls import path

from app import views

urlpatterns = [
    path("books", views.books, name="books"),
    path("book/<int:num>", views.book, name="book"),
    path("authors", views.authors, name="authors"),
    path("author/<int:num>", views.author, name="author"),
    path("publishers", views.publishers, name="publishers"),
    path("publisher/<int:num>", views.publisher, name="publisher"),
]
