def closest_pair(arr, target):
    closest_sum = float('inf')
    pair = ()

    for i in range(len(arr)):
        for j in range(i + 1, len(arr)):

            current_sum = arr[i] + arr[j]

            if abs(target - current_sum) < abs(target - closest_sum):
                closest_sum = current_sum
                pair = (arr[i], arr[j])

    return pair, closest_sum


arr = [10, 22, 28, 29, 30, 40]
target = 54

pair, total = closest_pair(arr, target)

print("Closest pair:", pair)
print("Sum:", total)