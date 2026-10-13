
def is_armstrong(num):
    if num < 0:
        return False

    digits = str(num)
    power = len(digits)
    total = 0

    for digit in digits:
        total += int(digit) ** power

    return total == num


num = int(input("Enter a number: "))

if is_armstrong(num):
    print(num, "is an Armstrong number")
else:
    print(num, "is not an Armstrong number")
