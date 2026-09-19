def quick_sort(arr):

    if len(arr) <= 1:
        return arr

    pivot = arr[-1]

    smaller = []
    greater = []

    for x in arr[:-1]:

        if x <= pivot:
            smaller.append(x)
        else:
            greater.append(x)

    return quick_sort(smaller) + [pivot] + quick_sort(greater)


arr = list(map(int, input("Enter numbers: ").split()))

print("Sorted array:", quick_sort(arr))