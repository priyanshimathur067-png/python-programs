def print_nos(n):
    if n== 0:
        return

    print_nos(n-1)
    print(n)

print_nos(5)