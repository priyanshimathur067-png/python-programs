
class Library:
    def __init__(self):
        self.books = []

    def add_book(self, book):
        if book not in self.books:
            self.books.append(book)
            print(book, "added successfully")
        else:
            print("Book already exists")

    def issue_book(self, book):
        if book in self.books:
            self.books.remove(book)
            print(book, "issued successfully")
        else:
            print("Book not available")

    def return_book(self, book):
        if book not in self.books:
            self.books.append(book)
            print(book, "returned successfully")
        else:
            print("Book is already available")

    def display_books(self):
        print("Available Books:")
        for book in self.books:
            print(book)


l1 = Library()

l1.add_book("Python Programming")
l1.add_book("Java Programming")
l1.issue_book("Python Programming")
l1.return_book("Python Programming")

l1.display_books()
