words = ["cat", "apple", "banana", "dog", "python"  ]

freq = {}

for x in words :
    freq[x] = freq.get(x, 0) + 1

print(freq)