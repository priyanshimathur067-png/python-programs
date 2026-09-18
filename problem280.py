arr = [7, 1, 5, 3, 6, 4]

minimum = arr[0]
max_difference = 0

for i in range(1, len(arr)):

    difference = arr[i] - minimum

    if difference > max_difference:
        max_difference = difference

    if arr[i] < minimum:
        minimum = arr[i]

print("Maximum difference:", max_difference)