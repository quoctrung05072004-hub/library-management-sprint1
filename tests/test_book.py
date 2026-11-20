import unittest
from library_system.book import Book

class TestBook(unittest.TestCase):
    def test_reject_empty_title(self):
        # Arrange
        title = "   "
        # Act + Assert
        with self.assertRaises(ValueError):
            Book(id=None, title=title, author="Nguyễn Nhật Ánh", isbn="978001")

    def test_reject_empty_author(self):
        # Arrange
        author = ""
        # Act + Assert
        with self.assertRaises(ValueError):
            Book(id=None, title="Dế Mèn phiêu lưu ký", author=author, isbn="978002")

    def test_reject_empty_isbn(self):
        # Arrange
        isbn = "   "
        # Act + Assert
        with self.assertRaises(ValueError):
            Book(id=None, title="Tuổi thơ dữ dội", author="Phùng Quán", isbn=isbn)

    def test_create_valid_book(self):
        # Arrange
        book_id = 1
        title = "Cho tôi xin một vé đi tuổi thơ"
        author = "Nguyễn Nhật Ánh"
        isbn = "9786042100014"

        # Act
        book = Book(id=book_id, title=title, author=author, isbn=isbn)

        # Assert
        self.assertEqual(book.id, 1)
        self.assertEqual(book.title, "Cho tôi xin một vé đi tuổi thơ")
        self.assertEqual(book.author, "Nguyễn Nhật Ánh")
        self.assertEqual(book.isbn, "9786042100014")

if __name__ == "__main__":
    unittest.main()