# IMproved method of insertion sort
arr = [23,34,54,12,11,21]
n = len(arr)
for i in range(1, n):
    insert_index = i
    current_value = arr[i]
    for j in range(i-1, -1, -1):
        if arr[j] > current_value:
            arr[j+1] = arr[j]    #shift right
            insert_index = j
        else:
            break
    arr[insert_index] = current_value
print("Sorted array is:", arr)