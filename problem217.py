def armstrong(num, original, total=0):
    if num == 0:
        return total == original

    digit = num % 10
    total = total + digit ** 3

    return armstrong(num // 10, original, total)


def sum_armstrong(current, n):
    if current > n:
        return 0

    if armstrong(current, current):
        return current + sum_armstrong(current + 1, n)

    return sum_armstrong(current + 1, n)


n = int(input("Enter N: "))

print("Sum:", sum_armstrong(1, n))