
def move_zeros(arr):
    result = []
    zero_count = 0

    for i in arr:
        if i == 0:
            zero_count += 1
        else:
            result.append(i)

    for i in range(zero_count):
        result.append(0)

    return result


n = int(input("Enter number of elements: "))
arr = []

for i in range(n):
    val = int(input("Enter element: "))
    arr.append(val)

print("Original list:", arr)
print("After moving zeros:", move_zeros(arr))
