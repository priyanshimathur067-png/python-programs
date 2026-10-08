def first_non_repeating(arr):
    for i in arr:
        if arr.count(i) == 1:
            return i

    return None


arr = [4, 5, 1, 4, 5, 2]

result = first_non_repeating(arr)

if result is not None:
    print("First non-repeating element:", result)
else:
    print("No non-repeating element")

