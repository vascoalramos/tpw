from django.contrib.auth import views as auth_views
from django.urls import path

from login import views

urlpatterns = [
    path("books", views.books, name="books"),
    path("book/<int:num>", views.book, name="book"),
    path("book-query", views.book_query, name="book-query"),
    path("authors", views.authors, name="authors"),
    path("author/<int:num>", views.author, name="author"),
    path("author-query", views.author_query, name="author-query"),
    path("publishers", views.publishers, name="publishers"),
    path("publisher/<int:num>", views.publisher, name="publisher"),
    path("publisher-query", views.publisher_query, name="publisher-query"),
    path("login/", auth_views.LoginView.as_view(template_name="login.html"), name="login"),
    path("logout/", auth_views.LogoutView.as_view(next_page="/"), name="logout"),
]
