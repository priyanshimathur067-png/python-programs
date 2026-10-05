def reverse(arr):
    reverse =[]
    for i in range(len(arr) -1, -1, -1):
        reverse.append(arr[i])
    return reverse
arr = [3,4,6,5,4]
print("The reverse of an array :", reverse(arr))
