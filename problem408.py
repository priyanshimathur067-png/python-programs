def alternate_numbers(arr):
    positive = []
    negative = []

    for num in arr:
        if num >= 0:
            positive.append(num)
        else:
            negative.append(num)

    result = []
    i = 0
    j = 0

    while i < len(positive) and j < len(negative):
        result.append(positive[i])
        result.append(negative[j])
        i += 1
        j += 1

    result.extend(positive[i:])
    result.extend(negative[j:])

    return result


arr = [1, 2, -3, -4, 5, -6]
print("Rearranged array:", alternate_numbers(arr))