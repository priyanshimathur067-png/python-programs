units = [120, 150, 98, 210, 175, 190]

total = sum(units)
average = total / len(units)

highest = max(units)
lowest = min(units)

print("Total consumption:", total)
print("Average consumption:", average)
print("Highest consumption:", highest)
print("Lowest consumption:", lowest)

print("Months above 180 units:")

for i in range(len(units)):
    if units[i] > 180:
        print("Month", i + 1, ":", units[i], "units")