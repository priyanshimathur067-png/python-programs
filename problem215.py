def armstrong(num, original, total=0):
    if num == 0:
        return total == original

    digit = num % 10
    total = total + digit ** 3

    return armstrong(num // 10, original, total)


def print_armstrong(current, n):
    if current > n:
        return

    if armstrong(current, current):
        print(current)

    print_armstrong(current + 1, n)


n = int(input("Enter N: "))

print_armstrong(1, n)