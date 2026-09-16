numbers = [1, 2, 2, 3, 4, 4, 5]

freq = {}

for x in numbers:
    freq[x] = freq.get(x, 0) + 1

for x in freq:
    if freq[x] == 1:
        print(x)