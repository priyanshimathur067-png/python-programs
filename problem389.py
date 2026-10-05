def find_duplicates(arr):
    duplicates = []

    for i in range(len(arr)):
        count = 0

        for j in range(len(arr)):
            if arr[i] == arr[j]:
                count += 1

        if count > 1 and arr[i] not in duplicates:
            duplicates.append(arr[i])

    return duplicates


print(find_duplicates([1, 2, 3, 2, 4, 1, 5]))