def first_repeating(arr):
    for i in arr:
        if arr.count(i) > 1:
            return i

    return -1


arr = [5, 3, 4, 3, 2, 5]
print(first_repeating(arr))