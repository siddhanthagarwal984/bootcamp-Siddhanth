from book import Book

# Creating multiple book instances
book1 = Book("1984", "George Orwell")
book2 = Book("To Kill a Mockingbird", "Harper Lee")
book3 = Book("The Catcher in the Rye", "J.D. Salinger")

# Checking book count
print(f"Total books created: {Book.get_book_count()}")
