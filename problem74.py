def uppercase(func):
    def wrapper():
        result = func()
        return result.upper()

    return wrapper


@uppercase
def message():
    return "welcome to python"


print(message())