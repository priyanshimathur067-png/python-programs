def shopping_cart(cart, quantity):

    total = 0

    for product, price in cart.items():

        if product in quantity:
            total += price * quantity[product]

    print("Subtotal:", total)

    if total > 5000:
        discount = total * 0.10
    else:
        discount = 0

    final_amount = total - discount

    print("Discount:", discount)
    print("Final Amount:", final_amount)

cart = {
    "Laptop": 50000,
    "Mouse": 500,
    "Keyboard": 1500
}

quantity = {
    "Laptop": 1,
    "Mouse": 2,
    "Keyboard": 1
}

shopping_cart(cart, quantity)