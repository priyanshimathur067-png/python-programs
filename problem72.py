def login_required(func):
    def wrapper():
        is_logged_in = True

        if is_logged_in:
            print("You are logged in. You can access the function.")
            func()
        else:
            print("You are not logged in. Please log in to access the function.")
    return wrapper

@login_required
def my_function():
    print("This is a function that requires login.")

my_function()