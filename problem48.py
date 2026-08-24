def process_order(customer, *items, discount=0, **details):

    print("Customer:", customer)

    print("\nItems:")
    for item in items:
        print("-", item)

    print("\nDiscount:", discount, "%")

    print("\nAdditional Details:")
    for key, value in details.items():
        print(key.title(), ":", value)


process_order(
    "Priyanshi",
    "Laptop",
    "Mouse",
    "Keyboard",
    discount=10,
    city="Bareilly",
    payment="UPI"
)