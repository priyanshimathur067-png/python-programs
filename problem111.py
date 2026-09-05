def fibonacci(a, b, n):
    if n == 0:
        return

    print(a, end=" ")

    fibonacci(b, a + b, n - 1)

fibonacci(0, 1, 8)