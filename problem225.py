def squares():
    for i in range(1, 6):
        yield i * i


for n in squares():
    print(n)