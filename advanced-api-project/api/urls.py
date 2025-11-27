from django.urls import path
from .views import (
    ListBooksView,
    BookDetailView,
    CreateBookView,
    UpdateBookView,
    DeleteBookView,
)

"""
URL Configuration for Book API
------------------------------
/books/               -> List all books
/books/<int:pk>/      -> Retrieve single book
/books/create/        -> Create a new book
/books/<int:pk>/edit/ -> Update an existing book
/books/<int:pk>/delete/ -> Delete a book
"""

urlpatterns = [
    path("books/", ListBooksView.as_view(), name="book-list"),
    path("books/<int:pk>/", BookDetailView.as_view(), name="book-detail"),
    path("books/create/", CreateBookView.as_view(), name="book-create"),
    path("books/<int:pk>/edit/", UpdateBookView.as_view(), name="book-update"),
    path("books/<int:pk>/delete/", DeleteBookView.as_view(), name="book-delete"),
]
