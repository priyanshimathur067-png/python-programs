numbers = [2, -3, 5, -2, -7, 8]

freq = {}

for x in numbers:
    if x >= 0:
        key = "positive"
    else:
        key = "negative"

    freq[key] = freq.get(key, 0) + 1

print(freq)