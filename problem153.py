from math import*
def count_digits(n):
    return int(log10(n)) + 1 if n > 0 else 1

count = count_digits(3254)
print("Number of digits:", count)
