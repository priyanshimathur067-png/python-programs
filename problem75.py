def positive_numbers(func):
    def wrapper(*args):
        if all(num > 0 for num in args):
            return func(*args)
        else:
            print("Negative number not allowed")

    return wrapper


@positive_numbers
def add(*numbers):
    print("Sum =", sum(numbers))


add(10, 20, 30)
add(10, -5, 20)