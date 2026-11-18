def move_zeros(arr):

    result = []
    count = 0

    for i in arr:

        if i != 0:
            result.append(i)
        else:
            count += 1

    for i in range(count):
        result.append(0)

    return result


n = int(input("Enter number of elements: "))
arr = []

for i in range(n):
    val = int(input("Enter element: "))
    arr.append(val)

print("Updated Array:", move_zeros(arr))