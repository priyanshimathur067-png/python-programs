def factorials():
    fact = 1

    for i in range(1, 6):
        fact = fact * i
        yield fact


for num in factorials():
    print(num)