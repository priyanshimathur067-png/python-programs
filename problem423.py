
def find_pairs(arr, target):
    found = False

    for i in range(len(arr)):
        for j in range(i + 1, len(arr)):
            if arr[i] + arr[j] == target:
                print(arr[i], arr[j])
                found = True

    if not found:
        print("No pairs found")


n = int(input("Enter number of elements: "))
arr = []

for i in range(n):
    val = int(input("Enter element: "))
    arr.append(val)

target = int(input("Enter target sum: "))

print("Pairs are:")
find_pairs(arr, target)
