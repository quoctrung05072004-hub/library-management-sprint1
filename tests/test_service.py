import unittest
from library_system.repository import BookRepository
from library_system.service import BookService

class TestBookService(unittest.TestCase):
    def setUp(self):
        self.repo = BookRepository()
        self.service = BookService(self.repo)

    def tearDown(self):
        self.repo.close()

    def test_add_book_success(self):
        # Arrange
        title, author, isbn = "Sách A", "Tác giả A", "111"
        # Act
        result = self.service.add_book(title, author, isbn)
        # Assert
        self.assertEqual("111", result.isbn)
        self.assertIsNotNone(result.id)

    def test_duplicate_isbn_is_rejected(self):
        # Arrange
        self.service.add_book("Sách A", "Tác giả A", "111")
        # Act + Assert
        with self.assertRaisesRegex(ValueError, "ISBN đã tồn tại"):
            self.service.add_book("Sách khác", "Tác giả khác", "111")

if __name__ == "__main__":
    unittest.main()
