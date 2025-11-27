# from rest_framework import generics, permissions
from .models import Book
from .serializers import BookSerializer

"""
ListBooksView
-------------
- Handles GET requests.
- Returns a list of all books.
- Permission: AllowAny (public read)
"""
class ListBooksView(generics.ListAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [permissions.AllowAny]


"""
BookDetailView
--------------
- Handles GET request for a single book by ID.
- Permission: AllowAny (public read)
"""
class BookDetailView(generics.RetrieveAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [permissions.AllowAny]


"""
CreateBookView
--------------
- Handles POST request to create a new book.
- Permission: Only authenticated users can create.
"""
class CreateBookView(generics.CreateAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [permissions.IsAuthenticated]

    # Custom behavior example: automatically clean and validate input
    def perform_create(self, serializer):
        """
        Custom hook to modify data before saving.
        """
        serializer.save()


"""
UpdateBookView
--------------
- Handles PUT/PATCH request to modify existing book.
- Permission: Only authenticated users can update.
"""
class UpdateBookView(generics.UpdateAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [permissions.IsAuthenticated]

    def perform_update(self, serializer):
        """
        Custom hook for update operations.
        """
        serializer.save()


"""
DeleteBookView
--------------
- Handles DELETE request to remove a book by ID.
- Permission: Only authenticated users can delete.
"""
class DeleteBookView(generics.DestroyAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [permissions.IsAuthenticated]
