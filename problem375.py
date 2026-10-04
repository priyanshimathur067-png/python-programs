def display(arr):
    for i in arr :
        print(i, end=" " )
n = int(input("Enter the no. of elements : "))
arr = []
for i in range(n):
    x = int(input("Enter the elements : ")) 
    arr.append(x)

display(arr)