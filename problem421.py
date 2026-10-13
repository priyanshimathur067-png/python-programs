
def frequency(arr):
    visited = []

    for i in arr:
        if i not in visited:
            count = 0

            for j in arr:
                if i == j:
                    count += 1

            print(i, "occurs", count, "times")
            visited.append(i)


n = int(input("Enter number of elements: "))
arr = []

for i in range(n):
    val = int(input("Enter element: "))
    arr.append(val)

frequency(arr)
