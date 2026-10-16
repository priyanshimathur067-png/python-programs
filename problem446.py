
def move_zeros(arr):
    result = []
    zeros = 0

    for i in arr:
        if i == 0:
            zeros += 1
        else:
            result.append(i)

    for i in range(zeros):
        result.append(0)

    return result


n = int(input("Enter number of elements: "))
arr = []

for i in range(n):
    val = int(input("Enter element: "))
    arr.append(val)

print("Updated array:", move_zeros(arr))
