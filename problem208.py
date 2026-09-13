def reverse_number(n, rev=0):
    if n == 0:
        return rev

    rev = rev * 10 + n % 10

    return reverse_number(n // 10, rev)


n = int(input("Enter number: "))
print("Reverse =", reverse_number(n))