def login_required(func):
    def wrapper(is_logged_in):
        if is_logged_in:
            return func()
        else:
            print("Please login first")
    return wrapper


@login_required
def dashboard():
    print("Welcome to your dashboard")


dashboard(True)
dashboard(False)