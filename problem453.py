def missing_number(arr, n):
    expected_sum = n * (n + 1) // 2
    actual_sum = 0

    for i in arr:
        actual_sum += i

    return expected_sum - actual_sum


size = int(input("Enter n: "))
arr = []

for i in range(size - 1):
    val = int(input("Enter element: "))
    arr.append(val)

print("Missing number:", missing_number(arr, size))