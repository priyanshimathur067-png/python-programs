def message_decorator(func):
    def wrapper():
        print("Function started")
        result = func()
        print("Function finished")
        return result

    return wrapper


@message_decorator
def calculate():
    return sum(range(1, 101))


print(calculate())