import math

n = int(input("Enter n: "))

log_sum = 0

for i in range(1, n + 1):
    log_sum += math.log10(i)

digits = math.floor(log_sum) + 1

print("Number of digits in factorial:", digits)