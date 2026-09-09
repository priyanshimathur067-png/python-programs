import math

n = int(input("Enter number: "))

digits = math.floor(math.log10(n))
first_digit = n // (10 ** digits)

print("First digit:", first_digit)