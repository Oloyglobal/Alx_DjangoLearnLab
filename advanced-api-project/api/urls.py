from django.urls import path
from .views import ListView, DetailView, CreateView, UpdateView, DeleteView

urlpatterns = [
    path("books/", ListView.as_view(), name="book-list"),
    path("books/<int:pk>/", DetailView.as_view(), name="book-detail"),
    path("books/create/", CreateView.as_view(), name="book-create"),
    path("books/update/<int:pk>/", UpdateView.as_view(), name="book-update"), 
    path("books/delete/<int:pk>/", DeleteView.as_view(), name="book-delete"),   
]


from django.urls import path
from .views import (
    BookListView,
    BookCreateView,
    BookUpdateView,
    BookDeleteView,
)

urlpatterns = [
    path("books/", BookListView.as_view(), name="book_list"),
    path("books/create/", BookCreateView.as_view(), name="book_create"),
    path("books/update/<int:pk>/", BookUpdateView.as_view(), name="book_update"),
    path("books/delete/<int:pk>/", BookDeleteView.as_view(), name="book_delete"),
]
