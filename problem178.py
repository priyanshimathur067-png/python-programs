num = int(input("Enter a number: "))

total = 0
product = 1

while num > 0:
    digit = num % 10
    total += digit
    product *= digit
    num //= 10

if total == product:
    print("Spy number")
else:
    print("Not a spy number")