products = [
    ["Laptop", 60000, 10],
    ["Phone", 30000, 25],
    ["Headphones", 5000, 40],
    ["Tablet", 20000, 15],
    ["Smartwatch", 8000, 30]
]

# Sort by discount in descending order
products.sort(key=lambda x: x[2], reverse=True)

print("Products with Highest Discount First")
print("-------------------------------------")

for product in products:
    print(
        product[0],
        "- Price:", product[1],
        "- Discount:", product[2], "%"
    )