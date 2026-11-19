import sqlite3
from library_system.book import Book

class BookRepository:
    def __init__(self, db_path=":memory:"):
        self.connection = sqlite3.connect(db_path)
        self.connection.row_factory = sqlite3.Row
        self.connection.execute("""
            CREATE TABLE IF NOT EXISTS books (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                title TEXT NOT NULL,
                author TEXT NOT NULL,
                isbn TEXT NOT NULL UNIQUE
            )
        """)
        self.connection.commit()

    def add(self, book):
        with self.connection:
            cursor = self.connection.execute(
                "INSERT INTO books (title, author, isbn) VALUES (?, ?, ?)",
                (book.title, book.author, book.isbn),
            )
        return Book(id=cursor.lastrowid, title=book.title, author=book.author, isbn=book.isbn)

    def find_by_isbn(self, isbn):
        row = self.connection.execute(
            "SELECT id, title, author, isbn FROM books WHERE isbn = ?", (isbn,)
        ).fetchone()
        return Book(**dict(row)) if row else None

    def get_all(self):
        rows = self.connection.execute(
            "SELECT id, title, author, isbn FROM books ORDER BY id"
        ).fetchall()
        return [Book(**dict(row)) for row in rows]

    def close(self):
        self.connection.close()
