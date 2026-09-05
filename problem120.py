def count_digit(n, target):
    if n == 0:
        return 0

    if n % 10 == target:
        return 1 + count_digit(n // 10, target)

    return count_digit(n // 10, target)


print(count_digit(122322, 2))