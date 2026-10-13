
def intersection(arr1, arr2):
    result = []

    for i in arr1:
        if i in arr2 and i not in result:
            result.append(i)

    return result


n1 = int(input("Enter size of first list: "))
arr1 = []

for i in range(n1):
    val = int(input("Enter element: "))
    arr1.append(val)

n2 = int(input("Enter size of second list: "))
arr2 = []

for i in range(n2):
    val = int(input("Enter element: "))
    arr2.append(val)

print("First list:", arr1)
print("Second list:", arr2)
print("Intersection:", intersection(arr1, arr2))
