from rest_framework import serializers
from django.utils import timezone
from .models import Author, Book

"""
BookSerializer:
- Serializes all fields from Book model.
- Includes custom validation to ensure publication_year is not in the future.
"""
class BookSerializer(serializers.ModelSerializer):

    def validate_publication_year(self, value):
        current_year = timezone.now().year
        if value > current_year:
            raise serializers.ValidationError("Publication year cannot be in the future.")
        return value

    class Meta:
        model = Book
        fields = ['id', 'title', 'publication_year', 'author']


"""
AuthorSerializer:
- Serializes the author's name.
- Nests BookSerializer to show all books written by the author.
- Demonstrates handling of nested relationships.
"""
class AuthorSerializer(serializers.ModelSerializer):
    books = BookSerializer(many=True, read_only=True)  # related_name="books" used here

    class Meta:
        model = Author
        fields = ['id', 'name', 'books']
