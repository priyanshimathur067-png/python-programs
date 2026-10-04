def second_smallest(arr):
    arr.sort()
    return arr[1]
n = int(input("How many elements : "))
arr =[]
for i in range(n) :
    val = int (input("Enter the elements : "))
    arr.append(val)
print("The second largest no. is : ", second_smallest(arr))
