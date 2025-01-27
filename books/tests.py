from django.test import TestCase
from django.urls import reverse
from .models import Author, Book, Genre

# Create your tests here.

class AuthorModelTest(TestCase):
    def setUp(self):
        self.author = Author.objects.create(first_name="John", last_name="Doe", birth_date="1970-01-01")

    def test_author_creation(self):
        self.assertEqual(self.author.first_name, "John")
        self.assertEqual(self.author.last_name, "Doe")
        self.assertEqual(self.author.birth_date, "1970-01-01")

class BookModelTest(TestCase):
    def setUp(self):
        self.author = Author.objects.create(first_name="John", last_name="Doe")
        self.book = Book.objects.create(
            title="Sample Book",
            author=self.author,
            genre="Fiction",
            publish_date="2020-01-01",
            summary="A sample book for testing purposes."
        )

    def test_book_creation(self):
        self.assertEqual(self.book.title, "Sample Book")
        self.assertEqual(self.book.author, self.author)
        self.assertEqual(self.book.genre, "Fiction")


class ViewTests(TestCase):
    def setUp(self):
        self.author = Author.objects.create(first_name="John", last_name="Doe")
        self.book = Book.objects.create(
            title="Sample Book",
            author=self.author,
            genre="Fiction",
            publish_date="2020-01-01",
            summary="A sample book for testing purposes."
        )

    def test_book_list_view(self):
        response = self.client.get(reverse("books:booklist"))  # Asume que la URL está nombrada.
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, self.book.title)

    def test_author_list_view(self):
        response = self.client.get(reverse("books:authorlist"))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, self.author.first_name)

    def test_book_detail_view(self):
        response = self.client.get(reverse("books:bookdetails", args=[self.book.id]))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, self.book.title)
        self.assertContains(response, self.author.first_name)