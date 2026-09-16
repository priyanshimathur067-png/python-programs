numbers = [1, 2, 2, 3, 3, 3, 4]

freq = {}

for x in numbers:
    freq[x] = freq.get(x, 0) + 1

minimum = float("inf")
answer = None

for x in freq:
    if freq[x] < minimum:
        minimum = freq[x]
        answer = x

print(answer)