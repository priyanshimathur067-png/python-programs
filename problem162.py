import math

n = int(input("Enter number: "))

digits = math.floor(math.log10(abs(n))) + 1

print("Number of digits:", digits)