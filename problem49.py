def food_order(customer, *items, **order_details):
    print("Customer:", customer)

    print("\nItems Ordered:")
    for item in items:
        print("-", item)

    print("\nOrder Details:")
    for key, value in order_details.items():
        print(key.title(), ":", value)


food_order(
    "Priyanshi",
    "Burger",
    "French Fries",
    "Cold Drink",
    address="Bareilly",
    payment="UPI",
    delivery="Express"
)