def reverse_number(n, rev=0):
    if n == 0:
        return rev

    return reverse_number(n // 10, rev * 10 + n % 10)


n = int(input("Enter number: "))

reverse = reverse_number(n)

if n == reverse:
    print("Palindrome")
else:
    print("Not Palindrome")