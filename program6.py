# fIND Average
numbers = []
avg = 0
n = int(input("How many numbers?"))
for i in range(n):
  value = int(input("Enter a number:"))
  numbers.append(value)
sum = 0
sum = sum + value
avg = sum / n
print("Average:", avg)
