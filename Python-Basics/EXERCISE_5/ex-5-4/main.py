from book import Book

# Creating book instances
book1 = Book("1984", "George Orwell")
book2 = Book("To Kill a Mockingbird", "Harper Lee")

# Printing book details
print(str(book1))  # Uses __str__
print(repr(book2))  # Uses __repr__
