def equilibrium_indices(arr):
    total = sum(arr)
    left_sum = 0
    result = []

    for i in range(len(arr)):
        right_sum = total - left_sum - arr[i]

        if left_sum == right_sum:
            result.append(i)

        left_sum += arr[i]

    return result


arr = [1, 3, 5, 2, 2]
print("Equilibrium indices:", equilibrium_indices(arr))