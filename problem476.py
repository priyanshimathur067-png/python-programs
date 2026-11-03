def count_element(arr):
    val = int(input("Enter element to count: "))
    c = arr.count(val)
    print("Count:", c)

n = int(input("Enter number of elements: "))
arr = []

for i in range(n):
    val = int(input("Enter element: "))
    arr.append(val)

count_element(arr)