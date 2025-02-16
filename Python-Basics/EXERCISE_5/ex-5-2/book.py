import re

class Book:
    def __init__(self, title: str, author: str):
        """Initializes a Book object with title and author."""
        self.title = title
        self.author = author

    @staticmethod
    def is_valid_isbn(isbn: str) -> bool:
        """Validates if the given ISBN-10 or ISBN-13 is correctly formatted."""
        return bool(re.match(r"^\d{9}[\dX]$|^\d{13}$", isbn))
