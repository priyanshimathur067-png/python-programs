def partition(arr, low, high):

    pivot = arr[high]

    i = low

    for j in range(low, high):

        if arr[j] < pivot:

            arr[i], arr[j] = arr[j], arr[i]

            i += 1

    arr[i], arr[high] = arr[high], arr[i]

    return i


def quick_sort(arr, low, high):

    if low < high:

        p = partition(arr, low, high)

        quick_sort(arr, low, p - 1)

        quick_sort(arr, p + 1, high)


arr = [12, 4, 7, 2, 9, 1]

quick_sort(arr, 0, len(arr) - 1)

print(arr)