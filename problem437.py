n = int(input("Enter a number: "))
n = abs(n)
count = 0

if n == 0:
    count = 1
else:
    while n > 0:
        count = count + 1
        n = n // 10

print("Number of digits:", count)