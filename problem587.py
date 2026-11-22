class Library:

    def __init__(self):

        self.books = {}

    def add_book(self, book):

        if book not in self.books:
            self.books[book] = True
            print(book, "added successfully!")
        else:
            print("Book already exists!")

    def borrow_book(self, book):

        if book not in self.books:
            print("Book not found!")

        elif self.books[book] == False:
            print("Book is already borrowed!")

        else:
            self.books[book] = False
            print(book, "borrowed successfully!")

    def return_book(self, book):

        if book not in self.books:
            print("Book not found!")

        elif self.books[book] == True:
            print("Book is already available!")

        else:
            self.books[book] = True
            print(book, "returned successfully!")

    def display_books(self):

        print("\nAvailable Books:")

        found = False

        for book, status in self.books.items():

            if status == True:
                print(book)
                found = True

        if not found:
            print("No books available")

library = Library()

library.add_book("Python")
library.add_book("Java")
library.add_book("React")

library.borrow_book("Python")

library.display_books()