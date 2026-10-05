def remove_duplicates(arr):
    result = []

    for i in arr:
        if i not in result:
            result.append(i)

    return result


print(remove_duplicates([1, 2, 2, 3, 1, 4]))