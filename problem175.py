import math

num = int(input("Enter a number: "))

original = num
total = 0

while num > 0:
    digit = num % 10
    total += math.factorial(digit)
    num //= 10

if total == original:
    print("Strong number")
else:
    print("Not a strong number")