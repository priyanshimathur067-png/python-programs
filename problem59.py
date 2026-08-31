def discount(func):
    def wrapper(amount):
        result = func(amount)

        if amount >= 2000:
            discount_amount = result * 0.20
            result -= discount_amount
            print("Discount: ₹", discount_amount)

        return result

    return wrapper


@discount
def calculate_bill(amount):
    print("Original bill: ₹", amount)
    return amount


amount = float(input("Enter shopping amount: "))

final_amount = calculate_bill(amount)

print("Final bill: ₹", final_amount)