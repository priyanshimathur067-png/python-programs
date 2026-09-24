products = [
    ("Laptop Bag", 1200),
    ("Mouse", 700),
    ("Keyboard", 1500),
    ("USB Cable", 300),
    ("Headphones", 900)
]

products.sort(key=lambda x: x[1])

print("Products from cheapest to expensive:")

for name, price in products:
    print(name, price)

print("\nProducts under ₹1000:")

for name, price in products:
    if price < 1000:
        print(name, price)