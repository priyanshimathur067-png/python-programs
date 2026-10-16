
def longest_increasing_run(arr):
    if len(arr) == 0:
        return 0

    current = 1
    longest = 1

    for i in range(1, len(arr)):
        if arr[i] > arr[i - 1]:
            current += 1
        else:
            current = 1

        if current > longest:
            longest = current

    return longest


n = int(input("Enter number of elements: "))
arr = []

for i in range(n):
    val = int(input("Enter element: "))
    arr.append(val)

print("Longest increasing run:",
      longest_increasing_run(arr))
