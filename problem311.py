hours = int(input("Enter parking hours: "))

if hours <= 2:
    fee = 30
elif hours <= 5:
    fee = 50
elif hours <= 8:
    fee = 80
else:
    fee = 100

print("Parking fee:", fee)