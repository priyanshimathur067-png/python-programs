def longest_consecutive(arr):
    if len(arr) == 0:
        return 0

    arr = list(set(arr))
    arr.sort()

    longest = 1
    current = 1

    for i in range(1, len(arr)):
        if arr[i] == arr[i - 1] + 1:
            current += 1
        else:
            current = 1

        if current > longest:
            longest = current

    return longest


arr = [100, 4, 200, 1, 3, 2]

print("Longest consecutive sequence:", longest_consecutive(arr))