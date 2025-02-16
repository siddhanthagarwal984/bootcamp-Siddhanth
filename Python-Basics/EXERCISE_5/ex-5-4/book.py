class Book:
    def __init__(self, title: str, author: str):
        """Initializes a Book object with title and author."""
        self.title = title
        self.author = author

    def __str__(self):
        """Returns a user-friendly string representation of the book."""
        return f"'{self.title}' by {self.author}"

    def __repr__(self):
        """Returns a formal string representation for debugging."""
        return f"Book(title={self.title!r}, author={self.author!r})"
