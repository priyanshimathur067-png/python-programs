# shopping cart
total = 0
while True :
    price = float(input("Enter product price: "))
    total += price

    choice = input("Do you want to add another product? (yes/no): ")

    if choice == "no":
        break

print("Total Bill = ",total)