
def find_missing(arr, n):
    expected_sum = n * (n + 1) // 2
    actual_sum = 0

    for i in arr:
        actual_sum += i

    return expected_sum - actual_sum


n = int(input("Enter the value of N: "))
arr = []

print("Enter", n - 1, "elements:")

for i in range(n - 1):
    val = int(input("Enter element: "))
    arr.append(val)

print("Missing number:", find_missing(arr, n))
