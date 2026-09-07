def calculate_bill(items, discount):
    total = sum (items.values())

    discount_amount = total * (discount / 100)
    after_discount = total - discount_amount

    gst = after_discount * 0.05
    final_amount = after_discount + gst

    return final_amount


items = {
    "Rice": 500,
    "Wheat": 300,
    "Sugar": 200,   
    "Milk": 150
}

print("Final Bill Amount:", calculate_bill(items, 10))