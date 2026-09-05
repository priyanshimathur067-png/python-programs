def is_sorted(arr, index):
    if index == len(arr) - 1:
        return True

    if arr[index] > arr[index + 1]:
        return False

    return is_sorted(arr, index + 1)


numbers = [10, 20, 30, 40, 50]

print(is_sorted(numbers, 0))