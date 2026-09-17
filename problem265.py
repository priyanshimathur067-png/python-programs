arr = [1, 2, 2, 3, 4, 4, 5]

frequency = {}

for num in arr:
    frequency[num] = frequency.get(num, 0) + 1

for num in frequency:
    if frequency[num] == 1:
        print(num)