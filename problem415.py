
while True:
    print("\n1. Say Hello")
    print("2. Say Welcome")
    print("3. Exit")

    choice = int(input("Enter your choice: "))

    if choice == 1:
        print("Hello!")
    elif choice == 2:
        print("Welcome!")
    elif choice == 3:
        print("Program ended")
        break
    else:
        print("Invalid choice")
