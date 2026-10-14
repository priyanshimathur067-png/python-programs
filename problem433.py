
def rotate_left(arr, k):
    if len(arr) == 0:
        return arr

    k = k % len(arr)
    result = []

    for i in range(k, len(arr)):
        result.append(arr[i])

    for i in range(k):
        result.append(arr[i])

    return result


n = int(input("Enter number of elements: "))
arr = []

for i in range(n):
    arr.append(int(input("Enter element: ")))

k = int(input("Enter rotation count: "))
print("Rotated list:", rotate_left(arr, k))
