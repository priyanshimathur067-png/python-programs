def separate_numbers(arr):
    negative = []
    others = []

    for i in arr:
        if i < 0:
            negative.append(i)
        else:
            others.append(i)

    return negative + others


n = int(input("Enter number of elements: "))
arr = []

for i in range(n):
    val = int(input("Enter element: "))
    arr.append(val)

print("Separated array:", separate_numbers(arr))