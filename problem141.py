def ticket_price(age, tickets):

    if age < 12:
        price = 100
    elif age >= 60:
        price = 120
    else:
        price = 200

    return price * tickets


age = int(input("Enter age: "))
tickets = int(input("Number of tickets: "))

print("Total Price:", ticket_price(age, tickets))