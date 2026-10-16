
def even_index_sum(arr):
    total = 0

    for i in range(len(arr)):
        if i % 2 == 0:
            total += arr[i]

    return total


n = int(input("Enter number of elements: "))
arr = []

for i in range(n):
    val = int(input("Enter element: "))
    arr.append(val)

print("Sum at even indices:", even_index_sum(arr))
