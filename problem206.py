def count_digits (n):
    if n == 0:
        return 0
    return 1 + count_digits(n // 10)

n = int (input("Enter a number: ") )

if n == 0:
    print("Number of digits in", n, "is: 1")
else:
    result = count_digits(n)
    print("Number of digits in", n, "is:", result)