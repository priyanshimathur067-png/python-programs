def odd_numbers():
    for i in range(1, 11):
        if i % 2 != 0:
            yield i


for n in odd_numbers():
    print(n)