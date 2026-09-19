def quick_sort(arr):

    if len(arr) <= 1:
        return arr

    pivot = arr[-1]

    left = []
    equal = []
    right = []

    for x in arr:
        if x < pivot:
            left.append(x)
        elif x == pivot:
            equal.append(x)
        else:
            right.append(x)

    return quick_sort(left) + equal + quick_sort(right)


arr = [10, 7, 8, 9, 1, 5]

print(quick_sort(arr))