def second_large(arr):
    arr.sort()
    return arr[-2]
n = int(input("How many elements : "))
arr =[]
for i in range(n) :
    val = int (input("Enter the elements : "))
    arr.append(val)
print("The second largest no. is : ", second_large(arr))
