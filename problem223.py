def even_numbers():
    for i in range(1, 11):
        if i % 2 == 0:
            yield i


for n in even_numbers():
    print(n)