def check_inventory(inventory, product, quantity):

    if product not in inventory:
        return "Product not available"

    if inventory[product] < quantity:
        return f"Only {inventory[product]} items available"

    inventory[product] -= quantity

    return f"Order successful. Remaining stock: {inventory[product]}"


inventory = {
    "Laptop": 10,
    "Mouse": 25,
    "Keyboard": 15
}

print(check_inventory(inventory, "Mouse", 5))
print(check_inventory(inventory, "Laptop", 15))