arr = [10, 25, 5, 40, 30]

largest = arr[0]
second = arr[0]

for num in arr:
    if num > largest:
        second = largest
        largest = num
    elif num > second and num != largest:
        second = num

print("Second largest:", second)