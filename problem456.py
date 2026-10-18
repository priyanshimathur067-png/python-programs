def maximum_difference(arr):
    if len(arr) < 2:
        return None

    minimum = arr[0]
    max_diff = arr[1] - arr[0]

    for i in range(1, len(arr)):
        difference = arr[i] - minimum

        if difference > max_diff:
            max_diff = difference

        if arr[i] < minimum:
            minimum = arr[i]

    return max_diff


n = int(input("Enter number of elements: "))
arr = []

for i in range(n):
    val = int(input("Enter element: "))
    arr.append(val)

print("Maximum difference:", maximum_difference(arr))