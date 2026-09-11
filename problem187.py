num = int(input("Enter a number: "))

for i in range(10):
    count = 0
    temp = num

    while temp > 0:
        digit = temp % 10

        if digit == i:
            count += 1

        temp //= 10

    if count > 0:
        print(i, "occurs", count, "times")