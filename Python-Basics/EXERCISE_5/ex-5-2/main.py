from book import Book

# Test ISBN validation without creating a Book instance
isbn1 = "123456789X"
isbn2 = "9781234567890"
isbn3 = "12345"

print(f"Is '{isbn1}' a valid ISBN? {Book.is_valid_isbn(isbn1)}")
print(f"Is '{isbn2}' a valid ISBN? {Book.is_valid_isbn(isbn2)}")
print(f"Is '{isbn3}' a valid ISBN? {Book.is_valid_isbn(isbn3)}")
