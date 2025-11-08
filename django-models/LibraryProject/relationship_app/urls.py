from django.urls import path
from .views import list_books  # <--- exact import ALX expects
from .views import LibraryDetailView  # import your class-based view

urlpatterns = [
    path('books/', list_books, name='list_books'),  # function-based view
    path('library/<int:pk>/', LibraryDetailView.as_view(), name='library_detail'),  # class-based view
]
