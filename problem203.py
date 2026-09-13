def sum (n):
    if n == 0 :
        return 0
    return n + sum(n - 1)

n = int (input("Enter a number: ") )
result = sum(n)
print("Sum of first", n, "numbers is:", result)
