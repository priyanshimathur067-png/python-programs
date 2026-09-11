num = int(input("Enter a number: "))

largest = -1
second = -1

while num > 0:
    digit = num % 10

    if digit > largest:
        second = largest
        largest = digit
    elif digit > second and digit != largest:
        second = digit

    num //= 10

if second == -1:
    print("Second largest digit does not exist")
else:
    print("Second largest digit:", second)