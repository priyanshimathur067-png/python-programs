num = int(input("Enter a number: "))
result = 0
place = 1

while num > 0:
    digit = num % 10

    if digit != 0:
        result = result + digit * place
        place *= 10

    num //= 10

print("After removing zeros:", result)