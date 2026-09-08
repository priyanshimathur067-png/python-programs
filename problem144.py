def shopping_cart(cart):

    total = 0

    for product, details in cart.items():
        price = details["price"]
        quantity = details["quantity"]

        total += price * quantity

    return total


cart = {
    "Laptop": {"price": 50000, "quantity": 1},
    "Mouse": {"price": 800, "quantity": 2},
    "Keyboard": {"price": 1500, "quantity": 1}
}

print("Total:", shopping_cart(cart))