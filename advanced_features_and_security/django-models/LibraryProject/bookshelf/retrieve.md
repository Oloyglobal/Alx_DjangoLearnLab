# Retrieve a Book instance

>>> from bookshelf.models import Book
>>> book = Book.objects.get(title="1984")
>>> book
<Book: 1984 by George Orwell (1949)>
# ✅ Successfully retrieved a single Book instance
