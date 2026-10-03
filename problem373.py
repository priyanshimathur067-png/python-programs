arr = []
n = int(input("Enter the no. of elements :"))
for i in range (n):
    x = int(input("Enter the elements: "))
    arr.append(x)
count = 0
for i in arr:
    if i % 2 == 0:
        count = count + 1
print("The no. of even nos are :",count)