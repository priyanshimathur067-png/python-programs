def power (a, n):
    if n == 0:
        return 1 
    return a * power(a, n - 1)

a = int (input("Enter a number: ") )
n = int (input("Enter the power: ") )
result = power(a, n)
print(a, "raised to the power", n, "is:", result)