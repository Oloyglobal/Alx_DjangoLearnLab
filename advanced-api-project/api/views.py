from rest_framework import generics, permissions
from .models import Book
from .serializers import BookSerializer

"""
ListView
--------
Handles GET requests (list all books)
"""
class ListView(generics.ListAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [permissions.AllowAny]


"""
DetailView
----------
Handles GET for a single book by ID
"""
class DetailView(generics.RetrieveAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [permissions.AllowAny]


"""
CreateView
----------
Handles POST to create a new book
"""
class CreateView(generics.CreateAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [permissions.IsAuthenticated]

    def perform_create(self, serializer):
        serializer.save()


"""
UpdateView
----------
Handles PUT/PATCH to update a book
"""
class UpdateView(generics.UpdateAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [permissions.IsAuthenticated]

    def perform_update(self, serializer):
        serializer.save()


"""
DeleteView
----------
Handles DELETE to remove a book
"""
class DeleteView(generics.DestroyAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [permissions.IsAuthenticated]
