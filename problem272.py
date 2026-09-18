# Selection Sort in Python
arr = [23,34,54,12,11,21]
n = len(arr)
for i in range(n-1):
    min_index = i
    for j in range(i+1, n):
        if arr[j] < arr[min_index]:
            min_index = j
    min_value = arr.pop(min_index)
    arr.insert(i, min_value)        
print("Sorted array is:", arr)        