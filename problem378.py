def even_count(arr):
    count = 0
    for i in arr:
        if i % 2 == 0:
            count = count + 1
    return count
n = int(input("How many elements :  ")) 
arr = []
for i in range(n):
    val = int(input("Enter the elements : "))
    arr.append(val)
print("The no. of even elements in an array is : ",even_count(arr)) 