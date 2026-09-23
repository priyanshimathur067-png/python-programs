stock = {
    "rice": 20,
    "sugar": 10,
    "oil": 5
}

print("1. Check Stock")
print("2. Add Stock")
print("3. Remove Stock")

choice = int(input("Enter your choice: "))

if choice == 1:
    product = input("Enter product name: ").lower()

    if product in stock:
        print("Available quantity:", stock[product])
    else:
        print("Product not found")

elif choice == 2:
    product = input("Enter product name: ").lower()
    quantity = int(input("Enter quantity to add: "))

    if product in stock:
        stock[product] += quantity
    else:
        stock[product] = quantity

    print("Updated stock:", stock)

elif choice == 3:
    product = input("Enter product name: ").lower()
    quantity = int(input("Enter quantity to remove: "))

    if product in stock:
        if quantity <= stock[product]:
            stock[product] -= quantity
            print("Updated stock:", stock)
        else:
            print("Not enough stock")
    else:
        print("Product not found")

else:
    print("Invalid choice")