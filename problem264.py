arr = [1, 2, 3, 2, 4, 1, 5]

frequency = {}

for num in arr:
    frequency[num] = frequency.get(num, 0) + 1

for num in frequency:
    if frequency[num] > 1:
        print(num)