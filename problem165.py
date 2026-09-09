import math

n = int(input("Enter number: "))

power = math.floor(math.log10(n))
result = 10 ** power

print("Highest power of 10:", result)