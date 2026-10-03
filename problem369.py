arr = []
n = int(input("Enter the no. of elements :"))
for i in range (n):
    x = int(input("Enter the elements"))
    arr.append(x)
total = 0 
for i in arr:
    total = total + i
print("Total :",total)