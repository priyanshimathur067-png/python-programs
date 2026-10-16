
def rotate_right(arr, k):
    n = len(arr)

    if n == 0:
        return arr

    k = k % n
    result = []

    for i in range(n - k, n):
        result.append(arr[i])

    for i in range(n - k):
        result.append(arr[i])

    return result


n = int(input("Enter number of elements: "))
arr = []

for i in range(n):
    val = int(input("Enter element: "))
    arr.append(val)

k = int(input("Enter rotation positions: "))

print("Rotated array:", rotate_right(arr, k))
