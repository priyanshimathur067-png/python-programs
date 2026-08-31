def service_charge(func):
    def wrapper(name, rent):
        amount = func(name, rent)

        charge = 100
        total = amount + charge

        print("Rent amount:", amount)
        print("Service charge:", charge)
        print("Total amount:", total)

    return wrapper


@service_charge
def pay_rent(name, rent):
    print("Payment received from", name)
    return rent


name = input("Enter tenant name: ")
rent = float(input("Enter rent amount: "))

pay_rent(name, rent)