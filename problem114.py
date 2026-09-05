def count_element(arr, target, index):
    if index == len(arr):
        return 0

    if arr[index] == target:
        return 1 + count_element(arr, target, index + 1)

    return count_element(arr, target, index + 1)


numbers = [2, 5, 2, 8, 2, 9]

print(count_element(numbers, 2, 0))