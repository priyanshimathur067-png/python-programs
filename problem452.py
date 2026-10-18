def find_leaders(arr):
    leaders = []

    for i in range(len(arr)):
        is_leader = True

        for j in range(i + 1, len(arr)):
            if arr[j] >= arr[i]:
                is_leader = False
                break

        if is_leader:
            leaders.append(arr[i])

    return leaders


n = int(input("Enter number of elements: "))
arr = []

for i in range(n):
    val = int(input("Enter element: "))
    arr.append(val)

print("Leaders:", find_leaders(arr))