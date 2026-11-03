def insert_element(arr):
    pos = int(input("Enter position: "))
    val = int(input("Enter value: "))
    arr.insert(pos, val)
    print("Updated list:", arr)

n = int(input("Enter number of elements: "))
arr = []

for i in range(n):
    val = int(input("Enter element: "))
    arr.append(val)

insert_element(arr)