import math

n = int(input("Enter number: "))

if n == 0:
    digits = 1
else:
    digits = math.floor(math.log10(abs(n))) + 1

if digits % 2 == 0:
    print("Even number of digits")
else:
    print("Odd number of digits")