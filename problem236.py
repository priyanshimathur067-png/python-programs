text = "Hey Himanshu, How are you?"

freq = {}
for x in text :
    freq[x] = freq.get(x,0) + 1

print(freq)