def product_digits(n):
    if n == 0:
        return 1

    return (n % 10) * product_digits(n // 10)


n = int(input("Enter number: "))

print("Product of digits =", product_digits(n))