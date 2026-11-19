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

if __name__ == "__main__":
    unittest.main()
