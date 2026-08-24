def place_order(*items, **customer):
    print("cUSTOMER DETAILS")
    for key, value in customer.items():
        print(key.title(), ":", value)

    print("\nOrdered Items: ")

    for item in items:
        print("-",item)

place_order(
    "Laptop",
    "Mouse",
    "Keyboard",
    name = "Priyanshi",
    city = "Noida",
    payment = "UPI"
)