def first_non_repeating(arr):
    for i in arr:
        if arr.count(i) == 1:
            return i

    return -1


arr = [4, 5, 1, 2, 1, 5, 4]
print(first_non_repeating(arr))