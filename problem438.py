n = int(input("Enter number of elements: "))
arr = []

for i in range(n):
    val = int(input("Enter an element: "))
    arr.append(val)

unique = list(set(arr))
unique.sort()

if len(unique) >= 2:
    print("Second largest:", unique[-2])
else:
    print("Second largest does not exist")