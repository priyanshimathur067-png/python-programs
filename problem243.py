text = "aabbcde"

freq = {}

for x in text:
    freq[x] = freq.get(x, 0) + 1

for x in text:
    if freq[x] == 1:
        print(x)
        break