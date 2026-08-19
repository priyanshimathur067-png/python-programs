#Calculate sum of the values stored in a list
sum = 0
numbers = []
n = int(input("How many numbers:"))
for i in range(n):
    num = int(input("Enter number: "))
    numbers.append(num)
    sum = sum + num
print("Your list is:",numbers)
print("Sum:",sum)    