books = {
    "Python Basics": 3,
    "DSA Handbook": 7,
    "Java Programming": 12,
    "Web Development": 5,
    "Database Systems": 15
}

highest_fine = 0
highest_book = ""

for book, days in books.items():

    if days <= 5:
        fine = days * 5

    elif days <= 10:
        fine = days * 10

    else:
        fine = days * 20

    print(book, "→ Fine: ₹", fine)

    if fine > highest_fine:
        highest_fine = fine
        highest_book = book

print("\nHighest fine:")
print(highest_book, "→ ₹", highest_fine)