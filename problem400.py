def frequency(arr):
    freq = {}

    for i in arr:
        if i in freq:
            freq[i] += 1
        else:
            freq[i] = 1

    for key in freq:
        print(key, "->", freq[key], "times")


arr = [2, 3, 2, 4, 3, 2]
frequency(arr)
