def delivery_charge(func):
    def wrapper(item, price):
        total = func(item, price)

        delivery = 40
        final_amount = total + delivery

        print("Food price: ₹", total)
        print("Delivery charge: ₹", delivery)
        print("Final amount: ₹", final_amount)

    return wrapper


@delivery_charge
def order_food(item, price):
    print("Order:", item)
    return price


item = input("Enter food item: ")
price = float(input("Enter price: "))

order_food(item, price)