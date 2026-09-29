price = float(input("Enter food price: "))
quantity = int(input("Enter quantity: "))

subtotal = price * quantity

if subtotal < 500:
    delivery = 40
else:
    delivery = 0

if subtotal > 1000:
    discount = subtotal * 0.10
else:
    discount = 0

final_bill = subtotal + delivery - discount

print("Subtotal:", subtotal)
print("Delivery charge:", delivery)
print("Discount:", discount)
print("Final bill:", final_bill)