def processing_charge(func):
    def wrapper(days):
        fine = func(days)

        charge = 10
        total = fine + charge

        print("Fine: ₹", fine)
        print("Processing charge: ₹", charge)
        print("Total: ₹", total)

    return wrapper


@processing_charge
def calculate_fine(days):
    return days * 5


days = int(input("Enter number of late days: "))

calculate_fine(days)