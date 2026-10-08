def max_frequency(arr):
    max_count = 0
    element = arr[0]

    for i in arr:
        count = arr.count(i)

        if count > max_count:
            max_count = count
            element = i

    return element


arr = [2, 3, 2, 4, 3, 2, 5]
print(max_frequency(arr))