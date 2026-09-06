def total_quantity(order):
    total = 0

    for item in order:
        if isinstance(item, dict):
            total += item["quantity"]

        elif isinstance(item, list):
            total += total_quantity(item)

    return total


order = [
    {"product": "Laptop", "quantity": 1},
    {"product": "Mouse", "quantity": 2},
    [
        {"product": "Keyboard", "quantity": 1},
        {"product": "USB Cable", "quantity": 3}
    ]
]

print("Total quantity:", total_quantity(order))