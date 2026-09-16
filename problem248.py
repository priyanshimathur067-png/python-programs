a = [1, 2, 3, 4, 5]
b = [3, 4, 5, 6, 7]

freq = {}

for x in a:
    freq[x] = freq.get(x, 0) + 1

for x in b:
    if x in freq:
        print(x)