import unittest
from library_system.repository import BookRepository
from library_system.book import Book
from library_system.search import BookSearch

class TestBookSearch(unittest.TestCase):
    def setUp(self):
        self.repo = BookRepository()
        self.repo.add(Book(None, "Python căn bản", "Nguyễn An", "111"))
        self.repo.add(Book(None, "Học SQL", "Trần Bình", "222"))
        self.search = BookSearch(self.repo)

    def tearDown(self):
        self.repo.close()

    def test_search_title_case_insensitive(self):
        # Arrange
        keyword = "PYTHON"
        # Act
        books = self.search.search_by_title(keyword)
        # Assert
        self.assertEqual(1, len(books))
        self.assertEqual("111", books[0].isbn)

    def test_search_author_returns_matching_book(self):
        # Arrange
        keyword = "Trần Bình"
        # Act
        books = self.search.search_by_author(keyword)
        # Assert
        self.assertEqual(1, len(books))
        self.assertEqual("222", books[0].isbn)

if __name__ == "__main__":
    unittest.main()
