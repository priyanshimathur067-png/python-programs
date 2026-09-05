def maximum(arr, n):
    if n == 1:
        return arr[0]

    return max(arr[n - 1], maximum(arr, n - 1))

numbers = [10, 25, 7, 45, 18]

print(maximum(numbers, len(numbers)))