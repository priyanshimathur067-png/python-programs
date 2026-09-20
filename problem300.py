def total_quantity(items, index=0):
    if index == len(items):
        return 0

    return items[index]["quantity"] + total_quantity(items, index + 1)


cart = [
    {"name": "Laptop", "quantity": 1},
    {"name": "Mouse", "quantity": 2},
    {"name": "Keyboard", "quantity": 1},
    {"name": "USB Cable", "quantity": 3}
]

print("Total items:", total_quantity(cart))