
def longest_sequence(arr):
    nums = set(arr)
    longest = 0

    for num in nums:
        if num - 1 not in nums:
            length = 1
            current = num

            while current + 1 in nums:
                current += 1
                length += 1

            longest = max(longest, length)

    return longest


arr = [100, 4, 200, 1, 3, 2]
print("Longest consecutive sequence length:",
      longest_sequence(arr))
