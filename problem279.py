arr = [2, 3, 2, 4, 3, 2, 5]

frequency = {}

for num in arr:
    if num in frequency:
        frequency[num] += 1
    else:
        frequency[num] = 1

print(frequency)