class Library:

    def __init__(self):
        self.books = ["Python", "Java", "C++"]

    def issue_book(self, book):
        if book in self.books:
            self.books.remove(book)
            print(book, "issued successfully")
        else:
            print("Book not available")

    def return_book(self, book):
        self.books.append(book)
        print(book, "returned successfully")

    def show_books(self):
        print("Available Books:", self.books)


l1 = Library()

l1.issue_book("Python")
l1.show_books()

l1.return_book("Python")
l1.show_books()