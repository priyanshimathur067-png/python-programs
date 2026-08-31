def validate_mobile(func):
    def wrapper(number, amount):
        if len(number) == 10 and number.isdigit():
            return func(number, amount)
        else:
            print("Invalid mobile number!")
    return wrapper


@validate_mobile
def recharge(number, amount):
    print(f"₹{amount} recharge successful for {number}")


number = input("Enter mobile number: ")
amount = float(input("Enter recharge amount: "))

recharge(number, amount)