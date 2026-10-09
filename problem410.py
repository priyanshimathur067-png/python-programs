def smallest_missing(arr):
    num_set = set(arr)
    number = 1

    while number in num_set:
        number += 1

    return number


arr = [3, 4, -1, 1]
print("Smallest missing positive:", smallest_missing(arr))