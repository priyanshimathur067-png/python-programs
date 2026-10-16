
def frequency(arr, target):
    count = 0

    for i in arr:
        if i == target:
            count += 1

    return count


n = int(input("Enter number of elements: "))
arr = []

for i in range(n):
    val = int(input("Enter element: "))
    arr.append(val)

target = int(input("Enter number to search: "))

print("Frequency:", frequency(arr, target))
