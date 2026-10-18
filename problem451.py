def even_odd_difference(arr):
    even_sum = 0
    odd_sum = 0

    for i in arr:
        if i % 2 == 0:
            even_sum += i
        else:
            odd_sum += i

    return even_sum - odd_sum


n = int(input("Enter number of elements: "))
arr = []

for i in range(n):
    val = int(input("Enter element: "))
    arr.append(val)

print("Difference:", even_odd_difference(arr))