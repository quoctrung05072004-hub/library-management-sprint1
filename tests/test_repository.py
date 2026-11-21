import unittest
from library_system.book import Book
from library_system.repository import BookRepository


class TestBookRepository(unittest.TestCase):
    def setUp(self):
        self.repo = BookRepository(":memory:")

    def tearDown(self):
        self.repo.close()

    def test_add_and_find_book_by_isbn(self):
        # 1. Arrange
        book = Book(id=None, title="Cong nghe Phan mem", author="Nguyen Van A", isbn="978-604-001")

        # 2. Act
        saved_book = self.repo.add(book)
        found_book = self.repo.find_by_isbn("978-604-001")

        # 3. Assert
        self.assertIsNotNone(saved_book.id)
        self.assertIsNotNone(found_book)
        self.assertEqual(found_book.title, "Cong nghe Phan mem")

    def test_count_books(self):
        # 1. Arrange
        self.repo.add(Book(id=None, title="Co so du lieu", author="Tran Thi B", isbn="978-604-002"))
        self.repo.add(Book(id=None, title="Lap trinh Python", author="Le Van C", isbn="978-604-003"))

        # 2. Act
        total = self.repo.count_books()

        # 3. Assert
        self.assertEqual(total, 2)

    def test_delete_book_by_isbn(self):
        # 1. Arrange
        self.repo.add(Book(id=None, title="Mang may tinh", author="Pham Van D", isbn="978-604-004"))

        # 2. Act
        deleted = self.repo.delete_by_isbn("978-604-004")
        remaining = self.repo.find_by_isbn("978-604-004")

        # 3. Assert
        self.assertTrue(deleted)
        self.assertIsNone(remaining)


if __name__ == "__main__":
    unittest.main()