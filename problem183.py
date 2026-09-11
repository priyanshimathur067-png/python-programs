num = int(input("Enter a number: "))
target = int(input("Enter digit to count: "))

count = 0

while num > 0:
    digit = num % 10

    if digit == target:
        count += 1

    num //= 10

print("Occurrence:", count)