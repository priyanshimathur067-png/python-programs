def calculate_bill(units):
    if units <= 100:
        bill = units * 3
    elif units <= 200:
        bill = 100 * 3 + (units - 100) * 5
    else:
        bill = 100 * 3 + 100 * 5 + (units - 200) * 7

    fixed_charge = 100
    return bill + fixed_charge


def display_bill(name, units):
    total = calculate_bill(units)

    print("\n--- ELECTRICITY BILL ---")
    print("Customer:", name)
    print("Units:", units)
    print("Total Bill: ₹", total)


name = input("Enter customer name: ")
units = int(input("Enter units consumed: "))

display_bill(name, units)