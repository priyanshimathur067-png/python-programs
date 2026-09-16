numbers = [1, 2, 3, 4, 5, 6, 7]

freq = {}

for x in numbers:
    if x % 2 == 0:
        key = "even"
    else:
        key = "odd"

    freq[key] = freq.get(key, 0) + 1

print(freq)