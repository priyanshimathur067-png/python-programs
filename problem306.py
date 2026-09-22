products = [
    ["Laptop", 55000],
    ["Phone", 25000],
    ["Headphones", 3000],
    ["Tablet", 18000],
    ["Keyboard", 2000]
]

# Sort by price
products.sort(key=lambda x: x[1])

print("Products from cheapest to most expensive:")

for product in products:
    print(product[0], "-", product[1])