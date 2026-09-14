def count_digits(num):
    if num == 0:
        return 0

    return 1 + count_digits(num // 10)


def armstrong(num, digits, original, total=0):
    if num == 0:
        return total == original

    digit = num % 10
    total = total + digit ** digits

    return armstrong(num // 10, digits, original, total)


num = int(input("Enter a number: "))

digits = count_digits(num)

if armstrong(num, digits, num):
    print("Armstrong number")
else:
    print("Not an Armstrong number")