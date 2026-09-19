def quick_sort(arr):

    if len(arr) <= 1:
        return arr

    pivot = arr[-1]

    greater = []
    smaller = []

    for x in arr[:-1]:

        if x >= pivot:
            greater.append(x)
        else:
            smaller.append(x)

    return quick_sort(greater) + [pivot] + quick_sort(smaller)


arr = [10, 7, 8, 9, 1, 5]

print(quick_sort(arr))