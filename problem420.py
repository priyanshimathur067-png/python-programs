
def frequency(arr):
    visited = []

    for i in arr:
        if i not in visited:
            count = 0

            for j in arr:
                if i == j:
                    count += 1

            print(i, "appears", count, "times")
            visited.append(i)


n = int(input("Enter the number of elements: "))
arr = []

for i in range(n):
    val = int(input("Enter an element: "))
    arr.append(val)

frequency(arr)
