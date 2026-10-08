def move_zeros(arr):
    result = []
    zeros = 0

    for i in arr:
        if i == 0:
            zeros += 1
        else:
            result.append(i)

    for i in range(zeros):
        result.append(0)

    return result


arr = [0, 5, 0, 3, 2, 0, 7]

print("Original array:", arr)
print("After moving zeros:", move_zeros(arr))