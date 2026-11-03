def remove_element(arr):
    val = int(input("Enter value to remove: "))

    if val in arr:
        arr.remove(val)
        print("Updated list:", arr)
    else:
        print("Element not found")

n = int(input("Enter number of elements: "))
arr = []

for i in range(n):
    val = int(input("Enter element: "))
    arr.append(val)

remove_element(arr)