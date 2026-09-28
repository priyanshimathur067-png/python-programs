products = {
    "Rice": 20,
    "Milk": 3,
    "Bread": 2,
    "Sugar": 10,
    "Oil": 4
}

print("Products requiring restocking:")

for product, quantity in products.items():

    if quantity < 5:
        print(product, "->", quantity, "left")  