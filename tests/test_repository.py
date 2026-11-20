import unittest
from library_system.book import Book
from library_system.repository import BookRepository

class TestBookRepository(unittest.TestCase):
    def setUp(self):
        self.repo = BookRepository()

    def tearDown(self):
        self.repo.close()

    def test_save_and_find_by_isbn(self):
        # Arrange
        book = Book(None, "Sách A", "Tác giả A", "111")
        # Act
        saved = self.repo.add(book)
        found = self.repo.find_by_isbn("111")
        # Assert
        self.assertEqual(saved.id, found.id)
        self.assertEqual("Sách A", found.title)

    def test_get_all_returns_two_books(self):
        # Arrange
        self.repo.add(Book(None, "Sách A", "Tác giả A", "111"))
        self.repo.add(Book(None, "Sách B", "Tác giả B", "222"))
        # Act
        books = self.repo.get_all()
        # Assert
        self.assertEqual(2, len(books))

if __name__ == "__main__":
    unittest.main()
