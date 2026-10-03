arr = []
n = int(input("Enter the no. of elements :"))
for i in range (n):
    x = int(input("Enter the elements"))
    arr.append(x)
smallest = arr[0] 
for i in arr:
   if  smallest > i:
    smallest = i
print("The smallest elements is :",smallest)