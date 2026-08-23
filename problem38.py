name = input("Enter customer name: ")
amount = input("Enter withdrawal amount: ")

message = f"Dear {name.title()}, your withdrawal request of ₹{amount} has been received."

print(message)