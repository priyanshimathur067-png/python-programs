def delivery_charge(distance, order_amount):

    if order_amount > 1000:
        return 0

    if distance <= 3:
        return 0
    elif distance <= 7:
        return 30
    else:
        return 50


distance = 8
order_amount = 700

print("Delivery Charge:", delivery_charge(distance, order_amount))