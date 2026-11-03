def pop_element(arr):
    pos = int(input("Enter index to remove: "))

    if 0 <= pos < len(arr):
        arr.pop(pos)
        print("Updated list:", arr)
    else:
        print("Invalid index")

n = int(input("Enter number of elements: "))
arr = []

for i in range(n):
    val = int(input("Enter element: "))
    arr.append(val)

pop_element(arr)