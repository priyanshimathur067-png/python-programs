water = [2.3, 2.7, 1.8, 2.1, 2.8, 1.9, 2.6]

target = 2.5

average = sum(water) / len(water)

target_days = 0

print("Average intake:", round(average, 2), "litres")

for day in range(len(water)):

    if water[day] >= target:
        target_days += 1

print("Target achieved on", target_days, "days")

print("\nDays below 2 litres:")

for day in range(len(water)):

    if water[day] < 2:
        print("Day", day + 1, ":", water[day], "litres")