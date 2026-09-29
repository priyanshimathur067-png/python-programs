usage = {
    "January": 120,
    "February": 150,
    "March": 135,
    "April": 180,
    "May": 200,
    "June": 160
}

total = sum(usage.values())
average = total / len(usage)

highest_month = max(usage, key=usage.get)

print("Average usage:", average)
print("Highest usage:", highest_month, usage[highest_month])

print("Months above average:")

for month, units in usage.items():
    if units > average:
        print(month, units)