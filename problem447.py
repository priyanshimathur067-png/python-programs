
def find_pairs(arr, target):
    pairs = []

    for i in range(len(arr)):
        for j in range(i + 1, len(arr)):
            if arr[i] + arr[j] == target:
                pairs.append((arr[i], arr[j]))

    return pairs


n = int(input("Enter number of elements: "))
arr = []

for i in range(n):
    val = int(input("Enter element: "))
    arr.append(val)

target = int(input("Enter target sum: "))

print("Pairs:", find_pairs(arr, target))
