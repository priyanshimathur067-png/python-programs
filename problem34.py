phone = input("Enter phone number: ")

if len(phone) == 10 and phone.isdigit():
    print("Valid phone number")
else:
    print("Invalid phone number")