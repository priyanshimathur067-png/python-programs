def is_prime(n):
    if n < 2:
        return False

    for i in range(2, n):
        if n % i == 0:
            return False

    return True


def prime_numbers(limit):
    for i in range(2, limit + 1):
        if is_prime(i):
            yield i


for number in prime_numbers(30):
    print(number)