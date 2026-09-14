n = int(input("Enter number: ") )
num = n
total = 0

nod = len(str(n))
while num > 0:
    ld = num % 10
    total += ld ** nod
    num = num // 10

if n == total:
    print("The number is a Armstrong  number.")
else :
    print("The number is not a Armstrong number.")