def add_element(arr):
    val = int(input("Enter element to add: "))
    arr.append(val)
    print("Updated list:", arr)

n = int(input("Enter number of elements: "))
arr = []

for i in range(n):
    val = int(input("Enter element: "))
    arr.append(val)

add_element(arr)