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
    
    def test_add_book_strips_whitespace(self):
        # Arrange + Act
        result = self.service.add_book("  Sách B  ", "  Tác giả B  ", "  222  ")
        # Assert
        self.assertEqual(result.title, "Sách B")
        self.assertEqual(result.author, "Tác giả B")
        self.assertEqual(result.isbn, "222")

    def test_add_book_empty_fields_raises_value_error(self):
        with self.assertRaises(ValueError):
            self.service.add_book("   ", "Tác giả A", "333")

        with self.assertRaises(ValueError):
            self.service.add_book("Sách C", "   ", "444")

        with self.assertRaises(ValueError):
            self.service.add_book("Sách D", "Tác giả D", "   ")
if __name__ == "__main__":
    unittest.main()
