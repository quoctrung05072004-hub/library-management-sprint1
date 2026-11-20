from library_system.book import Book

class BookService:
    def __init__(self, repository):
        self.repository = repository

    def add_book(self, title, author, isbn):
        book = Book(id=None, title=title.strip(), author=author.strip(), isbn=isbn.strip())
        if self.repository.find_by_isbn(book.isbn) is not None:
            raise ValueError("ISBN đã tồn tại trong thư viện")
        return self.repository.add(book)
