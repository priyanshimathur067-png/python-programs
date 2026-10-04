def count(arr):
    positive = 0
    negative = 0
    for i in arr:
        if i > 0:
            positive = positive + 1
        elif i < 0 :    
            negative = negative + 1
    return positive , negative        
n = int(input("How many elements :  ")) 
arr = []
for i in range(n):
    val = int(input("Enter the elements : "))
    arr.append(val)

positive , negative = count(arr)
print("The no. of positive elements in an array is : ", positive)
print("The no of negative elements is : " , negative) 