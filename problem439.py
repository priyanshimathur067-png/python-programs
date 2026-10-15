n = int(input("Enter number of elements: "))
arr = []

for i in range(n):
    val = int(input("Enter an element: "))
    arr.append(val)

frequency = {}

for i in arr:
    if i in frequency:
        frequency[i] = frequency[i] + 1
    else:
        frequency[i] = 1

print(frequency)