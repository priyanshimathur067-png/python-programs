arr = [10, 25, 7, 40, 15]

largest = float('-inf')
second = float('-inf')

for num in arr:
    if num > largest:
        second = largest
        largest = num
    elif num > second and num != largest:
        second = num

print("Second largest:", second)