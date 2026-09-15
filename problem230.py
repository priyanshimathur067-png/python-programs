def infinite_numbers():
    number = 1

    while True:
        yield number
        number += 1


g = infinite_numbers()

print(next(g))
print(next(g))
print(next(g))
print(next(g))
print(next(g))