import math

a = int(input("Enter a: "))
b = int(input("Enter b: "))

digits = math.floor(b * math.log10(a)) + 1

print("Number of digits:", digits)