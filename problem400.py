def closest_element(arr, target):
    closest = arr[0]

    for i in arr:
        if abs(i - target) < abs(closest - target):
            closest = i

    return closest


arr = [10, 22, 28, 29, 30, 40]
target = 25

print(closest_element(arr, target))