
total = 0

while True:
    n = int(input("Enter a number (0 to stop): "))
    total = total + n

    if n == 0:
        break

print("Total:", total)
