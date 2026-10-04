def smallest(arr):
    smallest = arr[0]
    for i in arr :
        if smallest > i:
            smallest = i 
    return smallest
n = int(input("Enter the no. of elements : "))
arr = []
for i in range (n):
    value = int(input("Enter the elements : "))
    arr.append(value)
print("Te smallest element in an array is:" ,smallest(arr))