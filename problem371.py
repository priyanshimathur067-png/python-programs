arr = []
n = int(input("Enter the no. of elements :"))
for i in range (n):
    x = int(input("Enter the elements : "))
    arr.append(x)
product = 1
for i in arr:
    product = product * i 
print("The product of all elements are :", product)
