def armstrong(num, original, total=0):
    if num == 0:
        return total == original

    digit = num % 10
    total = total + digit ** 3

    return armstrong(num // 10, original, total)


def count_armstrong(current, n):
    if current > n:
        return 0

    if armstrong(current, current):
        return 1 + count_armstrong(current + 1, n)

    return count_armstrong(current + 1, n)


n = int(input("Enter N: "))

print("Count:", count_armstrong(1, n))