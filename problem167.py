import math

n = int(input("Enter number: "))

if n != 0:
    digits = math.floor(math.log10(abs(n))) + 1
else:
    digits = 1

if digits == 3:
    print(True)
else:
    print(False)