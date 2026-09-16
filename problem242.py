text = "education"

freq = {}

for x in text:
    if x in "aeiou":
        freq[x] = freq.get(x, 0) + 1

print(freq)