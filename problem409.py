def longest_increasing(arr):
    if len(arr) == 0:
        return 0

    longest = 1
    current = 1

    for i in range(1, len(arr)):
        if arr[i] > arr[i - 1]:
            current += 1
        else:
            current = 1

        if current > longest:
            longest = current

    return longest


arr = [1, 2, 2, 3, 4, 1, 5]
print("Longest increasing length:", longest_increasing(arr))