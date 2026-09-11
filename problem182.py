num = int(input("Enter a number: "))
found = False

while num > 0:
    digit = num % 10

    if digit == 0:
        found = True
        break

    num //= 10

if found:
    print("Number contains zero")
else:
    print("Number does not contain zero")