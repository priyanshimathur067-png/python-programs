arr = []
n = int(input("Enter the no. of elements :"))
for i in range (n):
    x = int(input("Enter the elements: "))
    arr.append(x)
positive = 0
negative = 0
for i in arr:
    if i > 0:
        positive = positive + 1
    elif i < 0:
        negative = negative + 1
    
print("The no. of positive and negative  nos are :",positive, negative)