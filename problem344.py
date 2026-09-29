products = {
    "shirt": 700,
    "jeans": 1200,
    "shoes": 1800,
    "bag": 900
}

cart = ["shirt", "shoes", "bag"]

total = 0

for item in cart:
    total += products[item]

if total > 1500:
    delivery = 0
else:
    delivery = 80

final_amount = total + delivery

print("Product total:", total)
print("Delivery:", delivery)
print("Final amount:", final_amount)