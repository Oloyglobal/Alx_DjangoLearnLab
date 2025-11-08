from django.urls import path
from . import views
from .views import (
    list_books, 
    LibraryDetailView, 
    register, 
    CustomLoginView, 
    CustomLogoutView
)

urlpatterns = [
    # Book listing and library detail
    path('books/', list_books, name='list_books'),
    path('library/<int:pk>/', LibraryDetailView.as_view(), name='library_detail'),

    # Permission-protected book views
    path('books/add/', views.add_book, name='add_book'),
    path('books/edit/<int:pk>/', views.edit_book, name='edit_book'),
    path('books/delete/<int:pk>/', views.delete_book, name='delete_book'),

    # Authentication
    path('register/', register, name='register'),
    path('login/', CustomLoginView.as_view(template_name='relationship_app/login.html'), name='login'),
    path('logout/', CustomLogoutView.as_view(template_name='relationship_app/logout.html'), name='logout'),

    # Role-based views
    path('admin-view/', views.admin_view, name='admin_view'),
    path('librarian-view/', views.librarian_view, name='librarian_view'),
    path('member-view/', views.member_view, name='member_view'),
]
