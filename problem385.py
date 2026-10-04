def reverse_array(arr):
    reverse = []

    for i in range(len(arr) - 1, -1, -1):
        reverse.append(arr[i])

    return reverse


n = int(input("How many elements: "))

arr = []

for i in range(n):
    val = int(input("Enter the element: "))
    arr.append(val)

print("Original array:", arr)
print("Reversed array:", reverse_array(arr))