def digit_product(n):
    if n == 0:
        return 1

    return (n % 10) * digit_product(n // 10)


print(digit_product(234))