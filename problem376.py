def largest(arr):
    largest = 0
    for i in arr:
        if largest < i :
            largest = i
    return largest
n = int(input("Enter the no. of elements : "))
arr = []
for i in range(n):
    x = int(input("Enter the elements : "))
    arr.append(x)
print("The largest value in array is: ",largest(arr))
