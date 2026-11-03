def reverse_list(arr):
    arr.reverse()
    print("Reversed list:", arr)

n = int(input("Enter number of elements: "))
arr = []

for i in range(n):
    val = int(input("Enter element: "))
    arr.append(val)

reverse_list(arr)