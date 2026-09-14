def factors(num, i=1):
    if i > num:
        return

    if num % i == 0:
        print(i)

    factors(num, i + 1)


num = int(input("Enter a number: "))

factors(num)