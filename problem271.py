# Python program for implementation of Bubble Sort

arr = [23,17,12,34,25]
n = len(arr)
for i in range (n-1):
    for j in range (n-i-1):
        if arr[j] > arr[j+1]:
            arr[j], arr[j+1] = arr[j+1], arr[j]
print("Sorted array is:", arr)         ]