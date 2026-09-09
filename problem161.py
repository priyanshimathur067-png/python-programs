import math

n = int(input("Enter a number: "))

if n == 0:
    digits = 1
else:
    digits = math.floor(math.log10(abs(n))) + 1

print("Number of digits:", digits)