import random


def quick_sort(arr):

    if len(arr) <= 1:
        return arr

    pivot = random.choice(arr)

    left = []
    middle = []
    right = []

    for x in arr:

        if x < pivot:
            left.append(x)

        elif x == pivot:
            middle.append(x)

        else:
            right.append(x)

    return quick_sort(left) + middle + quick_sort(right)


arr = [10, 7, 8, 9, 1, 5]

print(quick_sort(arr))