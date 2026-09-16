num = [1, 2, 2, 3, 2, 5, 6, 4, 4, 4]
freq = {}

for x in num:

    freq[x] = freq.get(x, 0) + 1

for x in freq :
    if freq[x] >1 :    
        
        print(x, ":", freq[x])