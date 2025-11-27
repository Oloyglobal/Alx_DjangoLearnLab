from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase
from .models import Book, Author
from django.contrib.auth.models import User


class BookAPITestCase(APITestCase):
    def setUp(self):
        # Create test user
        self.user = User.objects.create_user(username='testuser', password='testpass')

        # Create authors
        self.author1 = Author.objects.create(name='Chinua Achebe')
        self.author2 = Author.objects.create(name='Wole Soyinka')

        # Create books
        self.book1 = Book.objects.create(title='Things Fall Apart', publication_year=1958, author=self.author1)
        self.book2 = Book.objects.create(title='No Longer at Ease', publication_year=1960, author=self.author1)
        self.book3 = Book.objects.create(title='Death and the King’s Horseman', publication_year=1975, author=self.author2)

    # ---------------------------
    # LIST BOOKS
    # ---------------------------
    def test_list_books(self):
        url = reverse('book-list')
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 3)

    # ---------------------------
    # CREATE BOOK
    # ---------------------------
    def test_create_book_authenticated(self):
        self.client.login(username='testuser', password='testpass')
        url = reverse('book-create')
        data = {
            'title': 'A New Book',
            'publication_year': 2020,
            'author': self.author1.id
        }
        response = self.client.post(url, data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Book.objects.count(), 4)

    def test_create_book_unauthenticated(self):
        url = reverse('book-create')
        data = {'title': 'A New Book', 'publication_year': 2020, 'author': self.author1.id}
        response = self.client.post(url, data)
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)

    # ---------------------------
    # RETRIEVE BOOK
    # ---------------------------
    def test_retrieve_book(self):
        url = reverse('book-detail', args=[self.book1.id])
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['title'], self.book1.title)

    # ---------------------------
    # UPDATE BOOK
    # ---------------------------
    def test_update_book_authenticated(self):
        self.client.login(username='testuser', password='testpass')
        url = reverse('book-update', args=[self.book1.id])
        data = {'title': 'Updated Title', 'publication_year': 1960, 'author': self.author1.id}
        response = self.client.put(url, data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.book1.refresh_from_db()
        self.assertEqual(self.book1.title, 'Updated Title')

    def test_update_book_unauthenticated(self):
        url = reverse('book-update', args=[self.book1.id])
        data = {'title': 'Updated Title', 'publication_year': 1960, 'author': self.author1.id}
        response = self.client.put(url, data)
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)

    # ---------------------------
    # DELETE BOOK
    # ---------------------------
    def test_delete_book_authenticated(self):
        self.client.login(username='testuser', password='testpass')
        url = reverse('book-delete', args=[self.book1.id])
        response = self.client.delete(url)
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertEqual(Book.objects.count(), 2)

    def test_delete_book_unauthenticated(self):
        url = reverse('book-delete', args=[self.book1.id])
        response = self.client.delete(url)
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)

    # ---------------------------
    # FILTERING, SEARCHING, ORDERING
    # ---------------------------
    def test_filter_books_by_title(self):
        url = reverse('book-list') + '?title=Things Fall Apart'
        response = self.client.get(url)
        self.assertEqual(len(response.data), 1)
        self.assertEqual(response.data[0]['title'], 'Things Fall Apart')

    def test_search_books(self):
        url = reverse('book-list') + '?search=Wole'
        response = self.client.get(url)
        self.assertEqual(len(response.data), 1)
        self.assertEqual(response.data[0]['title'], 'Death and the King’s Horseman')

    def test_order_books(self):
        url = reverse('book-list') + '?ordering=publication_year'
        response = self.client.get(url)
        self.assertEqual(response.data[0]['publication_year'], 1958)
