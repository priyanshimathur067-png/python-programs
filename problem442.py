
def greater_than_average(arr):
    avg = sum(arr) / len(arr)
    result = []

    for i in arr:
        if i > avg:
            result.append(i)

    return result


n = int(input("Enter number of elements: "))
arr = []

for i in range(n):
    val = int(input("Enter element: "))
    arr.append(val)

print("Elements greater than average:",
      greater_than_average(arr))
