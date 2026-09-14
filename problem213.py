def arm(n):
    num = n
    total = 0

    nod = len(str(n))
    while num > 0:
        ld = n % 10
        total += ld ** nod
        n = n// 10

    if total == num:
        return True
    else:
        return False


number = int(input("Enter number: "))
if arm(number):
    print("The number is an Armstrong number.")
else:
    print("The number is not an Armstrong number.")