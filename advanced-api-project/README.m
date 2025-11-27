# Advanced API Project — Generic Views Task

This project implements CRUD operations for the Book model using Django REST Framework generic views.

## Features
- List all books (public)
- Retrieve a single book (public)
- Create, update, delete books (authenticated users only)
- Custom behavior using `perform_create` and `perform_update`
- DRF permissions integrated directly in views

## Endpoints
/books/  
/books/<pk>/  
/books/create/  
/books/<pk>/edit/  
/books/<pk>/delete/
