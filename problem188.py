num = int(input("Enter a number: "))

previous = num % 10
num //= 10

ascending = True

while num > 0:
    digit = num % 10

    if digit >= previous:
        ascending = False
        break

    previous = digit
    num //= 10

if ascending:
    print("Digits are in ascending order")
else:
    print("Digits are not in ascending order")