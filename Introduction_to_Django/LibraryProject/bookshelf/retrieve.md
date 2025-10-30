# Retrieve a Book instance

>>> from bookshelf.models import Book
>>> books = Book.objects.all()
>>> books
<QuerySet [<Book: 1984 by George Orwell (1949)>]>
# ✅ Successfully retrieved all Book instances
