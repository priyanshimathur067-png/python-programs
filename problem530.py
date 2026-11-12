class Library:
    def __init__(self, name):
        self.name = name

    class Book:
        def __init__(self, title, author):
            self.title = title
            self.author = author

l = Library("Central Library")
b = l.Book("Python Programming", "Guido")

print(l.name)
print(b.title)
print(b.author)