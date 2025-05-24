class Book:
    total_books = 0  # Class variable to keep track of the total number of books

    def __init__(self, title, author):
        self.title = title
        self.author = author
        Book.increment_book_count()  # Call class method to increment the book count

    @classmethod
    def increment_book_count(cls):
        cls.total_books += 1  # Increase the count of books

# Create new book instances with updated details
book1 = Book("The Catcher in the Rye", "J.D. Salinger")
book2 = Book("Pride and Prejudice", "Jane Austen")
book3 = Book("The Great Gatsby", "F. Scott Fitzgerald")

# Print total number of books
print("Total books:", Book.total_books)