from django.urls import path
from .views import (
    list_books,
    LibraryDetailView,
    register,
    CustomLoginView,
    CustomLogoutView,
    add_book,
    edit_book,
    delete_book,
    admin_view,
    librarian_view,
    member_view,
)

urlpatterns = [
    # Book listing and library detail
    path('books/', list_books, name='list_books'),
    path('library/<int:pk>/', LibraryDetailView.as_view(), name='library_detail'),

    # Permission-protected book views
    path('books/add/', add_book, name='add_book'),
    path('books/edit/<int:pk>/', edit_book, name='edit_book'),
    path('books/delete/<int:pk>/', delete_book, name='delete_book'),

    # Authentication
    path('register/', register, name='register'),
    path('login/', CustomLoginView.as_view(template_name='relationship_app/login.html'), name='login'),
    path('logout/', CustomLogoutView.as_view(template_name='relationship_app/logout.html'), name='logout'),

    # Role-based views
    path('admin-view/', admin_view, name='admin_view'),
    path('librarian-view/', librarian_view, name='librarian_view'),
    path('member-view/', member_view, name='member_view'),
]
