arr = [10, 25, 7, 40, 15]

smallest = float('inf')
second = float('inf')

for num in arr:
    if num < smallest:
        second = smallest
        smallest = num
    elif num < second and num != smallest:
        second = num

print("Second smallest:", second)