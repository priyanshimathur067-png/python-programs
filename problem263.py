arr = [1, 2, 2, 3, 1, 2]

frequency = {}

for num in arr:
    if num in frequency:
        frequency[num] += 1
    else:
        frequency[num] = 1

print(frequency)