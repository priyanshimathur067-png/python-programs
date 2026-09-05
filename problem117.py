def first_occurrence(arr, target, index):
    if index == len(arr):
        return -1

    if arr[index] == target:
        return index

    return first_occurrence(arr, target, index + 1)


numbers = [10, 20, 30, 20, 40]

print(first_occurrence(numbers, 20, 0))