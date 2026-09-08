import math

def count_digits(n):
    if n == 0:
        return 1

    return int(math.log10(n)) + 1


n = int(input("Enter a number: "))

print("Number of digits =", count_digits(n))