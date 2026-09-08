def hotel_bill(room_price, nights, food_bill=0):

    room_cost = room_price * nights
    total = room_cost + food_bill

    tax = total * 12 / 100

    final_bill = total + tax

    return final_bill


print("Hotel Bill:", hotel_bill(2500, 3, 1500))