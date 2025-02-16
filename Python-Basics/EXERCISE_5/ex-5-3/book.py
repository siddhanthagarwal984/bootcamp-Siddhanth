import re

class Book:
    book_count = 0  # Class variable to track number of books

    def __init__(self, title: str, author: str):
        """Initializes a Book object with title and author, and updates book count."""
        self.title = title
        self.author = author
        Book.book_count += 1

    @staticmethod
    def is_valid_isbn(isbn: str) -> bool:
        """Validates if the given ISBN-10 or ISBN-13 is correctly formatted."""
        return bool(re.match(r"^\d{9}[\dX]$|^\d{13}$", isbn))

    @classmethod
    def get_book_count(cls):
        """Returns the total number of Book instances created."""
        return cls.book_count
