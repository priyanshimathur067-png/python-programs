def maximum_product(arr):
    if len(arr) < 2:
        return None

    max_product = arr[0] * arr[1]

    for i in range(len(arr)):
        for j in range(i + 1, len(arr)):
            product = arr[i] * arr[j]

            if product > max_product:
                max_product = product

    return max_product


arr = [3, 5, -2, 8, -10]
print("Maximum product:", maximum_product(arr))