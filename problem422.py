
def remove_duplicates(arr):
    result = []

    for i in arr:
        if i not in result:
            result.append(i)

    return result


n = int(input("Enter number of elements: "))
arr = []

for i in range(n):
    val = int(input("Enter element: "))
    arr.append(val)

print("Original list:", arr)
print("List without duplicates:", remove_duplicates(arr))
