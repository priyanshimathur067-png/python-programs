arr = []
n = int(input("Enter the no. of elements :"))
for i in range (n):
    x = int(input("Enter the elements"))
    arr.append(x)
largest = 0
for i in arr:
    if i > largest:
        largest = i
print("The largest element is :" , largest)