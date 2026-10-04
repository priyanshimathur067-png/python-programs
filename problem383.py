def reverse_array(arr):
    return arr[::-1]


n = int(input("How many elements: "))

arr = []

for i in range(n):
    val = int(input("Enter the element: "))
    arr.append(val)

print("Original array:", arr)
print("Reversed array:", reverse_array(arr))