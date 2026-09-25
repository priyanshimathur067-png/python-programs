sales = {
    "Laptop": 15,
    "Mobile": 32,
    "Tablet": 18,
    "Keyboard": 25,
    "Mouse": 40
}

total = sum(sales.values())

most_sold = max(sales, key=sales.get)
least_sold = min(sales, key=sales.get)

print("Total products sold:", total)
print("Most sold product:", most_sold)
print("Least sold product:", least_sold)

print("Products sold above 20 units:")

for product, quantity in sales.items():
    if quantity > 20:
        print(product, ":", quantity)