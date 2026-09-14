def armstrong(num, digits, total=0):
    if num == 0:
        return total

    digit = num % 10
    total = total + digit ** digits

    return armstrong(num // 10, digits, total)


number = int(input("Enter a number: "))

digits = len(str(number))

result = armstrong(number, digits)

if result == number:
    print("Armstrong number")
else:
    print("Not an Armstrong number")