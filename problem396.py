def count_unique(arr):
    count = 0

    for i in arr:
        if arr.count(i) == 1:
            count += 1

    return count


arr = [1, 2, 2, 3, 4, 4, 5]
print(count_unique(arr))