total = 0

while True:
    print("\n1. Pizza - ₹200")
    print("2. Burger - ₹100")
    print("3. Coffee - ₹50")
    print("4. Exit")

    choice = int(input("Enter your choice: "))

    if choice == 1:
        total += 200
        print("Pizza added")
    elif choice == 2:
        total += 100
        print("Burger added")
    elif choice == 3:
        total += 50
        print("Coffee added")
    elif choice == 4:
        break
    else:
        print("Invalid choice")

print("Total bill =", total)