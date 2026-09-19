def quick_sort(arr):

    if len(arr) <= 1:
        return arr

    pivot = arr[0]

    smaller = []
    greater = []

    for x in arr[1:]:

        if x <= pivot:
            smaller.append(x)
        else:
            greater.append(x)

    return quick_sort(smaller) + [pivot] + quick_sort(greater)


arr = [10, 7, 8, 9, 1, 5]

print(quick_sort(arr))