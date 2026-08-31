def validate_password(func):
    def wrapper(username, password):
        if len(password) >= 8:
            return func(username, password)
        else:
            print("Password must contain at least 8 characters!")
    return wrapper


@validate_password
def register(username, password):
    print("Registration successful!")
    print("Username:", username)


username = input("Enter username: ")
password = input("Enter password: ")

register(username, password)