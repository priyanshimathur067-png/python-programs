def find_index(arr):
    val = int(input("Enter element to search: "))

    if val in arr:
        print("Index:", arr.index(val))
    else:
        print("Element not found")

n = int(input("Enter number of elements: "))
arr = []

for i in range(n):
    val = int(input("Enter element: "))
    arr.append(val)

find_index(arr)