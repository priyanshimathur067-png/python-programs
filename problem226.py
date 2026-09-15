def divisible_by_3():
    for i in range(1, 31):
        if i % 3 == 0:
            yield i


for n in divisible_by_3():
    print(n)