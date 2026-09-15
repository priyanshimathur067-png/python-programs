def divisible_by_5():
    for i in range(1, 51):
        if i % 5 == 0:
            yield i


for num in divisible_by_5():
    print(num)