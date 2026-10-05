def rotate(arr, k):
    n = len(arr)
    k = k % n

    result = []

    for i in range(n - k, n):
        result.append(arr[i])

    for i in range(0, n - k):
        result.append(arr[i])

    return result


arr = [1, 2, 3, 4, 5]
k = 2

print(rotate(arr, k))