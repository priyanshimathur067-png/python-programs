num = int(input("Enter a number: "))

smallest = 10
second = 10

while num > 0:
    digit = num % 10

    if digit < smallest:
        second = smallest
        smallest = digit
    elif digit < second and digit != smallest:
        second = digit

    num //= 10

if second == 10:
    print("Second smallest digit does not exist")
else:
    print("Second smallest digit:", second)