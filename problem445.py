
def common_elements(a, b):
    result = []

    for i in a:
        if i in b and i not in result:
            result.append(i)

    return result


n = int(input("Enter size of first array: "))
a = []

for i in range(n):
    val = int(input("Enter element: "))
    a.append(val)

m = int(input("Enter size of second array: "))
b = []

for i in range(m):
    val = int(input("Enter element: "))
    b.append(val)

print("Common elements:", common_elements(a, b))
