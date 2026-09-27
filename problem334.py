daily_usage = [12, 15, 18, 11, 25, 30, 28]

total = sum(daily_usage)
average = total / len(daily_usage)

print("Total usage:", total)
print("Average usage:", average)

for day, usage in enumerate(daily_usage, start=1):
    if usage > average:
        print("Day", day, "→ Above average:", usage)