# from django.db import models

# # Create your models here.
from django.db import models
from django.utils import timezone

"""
Author Model:
- Represents a book author.
- Has only one field: name.
"""
class Author(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name


"""
Book Model:
- Each book has a title, publication year, and a foreign key reference to Author.
- Represents a one-to-many relationship: One Author → Many Books.
"""
class Book(models.Model):
    title = models.CharField(max_length=255)
    publication_year = models.IntegerField()
    author = models.ForeignKey(Author, related_name="books", on_delete=models.CASCADE)

    def __str__(self):
        return self.title
