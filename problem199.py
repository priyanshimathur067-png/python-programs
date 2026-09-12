numbers = [2, 3, 2, 5, 2, 3, 4, 3, 3]

most_frequent = numbers[0]
max_count = 0

for num in numbers:
    count = 0

    for x in numbers:
        if x == num:
            count += 1

    if count > max_count:
        max_count = count
        most_frequent = num

print("Most frequent =", most_frequent)
print("Frequency =", max_count)