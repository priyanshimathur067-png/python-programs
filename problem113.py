def minimum(arr, n):
    if n == 1:
        return arr[0]

    return min(arr[n - 1], minimum(arr, n - 1))

numbers = [10, 25, 7, 45, 18]

print(minimum(numbers, len(numbers))