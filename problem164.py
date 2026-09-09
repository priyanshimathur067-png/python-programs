import math

n = float(input("Enter number: "))

integer_part = int(n)

if integer_part == 0:
    before = 1
else:
    before = math.floor(math.log10(integer_part)) + 1

text = str(n)
after = len(text.split('.')[1])

print("Digits before decimal:", before)
print("Digits after decimal:", after)