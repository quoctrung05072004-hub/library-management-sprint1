from dataclasses import dataclass
from typing import Optional

@dataclass
class Book:
    id: Optional[int]
    title: str
    author: str
    isbn: str

    def __post_init__(self):
        if not self.title or not self.title.strip():
            raise ValueError("Tên sách không được để trống")
        if not self.author or not self.author.strip():
            raise ValueError("Tên tác giả không được để trống")
        if not self.isbn or not self.isbn.strip():
            raise ValueError("ISBN không được để trống")
