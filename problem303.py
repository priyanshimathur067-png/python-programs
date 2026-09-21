arr = [0, 1, 0, 3, 12]

position = 0

for num in arr:
    if num != 0:
        arr[position] = num
        position += 1

while position < len(arr):
    arr[position] = 0
    position += 1

print(arr)