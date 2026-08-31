logged_in = False


def login_required(func):
    def wrapper(name):
        if logged_in:
            return func(name)
        else:
            print("Please login before starting the exam.")

    return wrapper


def login():
    global logged_in

    username = input("Enter username: ")
    password = input("Enter password: ")

    if username == "student" and password == "1234":
        logged_in = True
        print("Login successful!")
    else:
        print("Invalid username or password!")


@login_required
def start_exam(name):
    print(f"\nWelcome {name}!")
    print("Your exam has started.")
    print("You have 60 minutes.")


print("----- ONLINE EXAM -----")
print("1. Login")
print("2. Start Exam")

choice = input("Enter choice: ")

if choice == "1":
    login()

    if logged_in:
        name = input("Enter your name: ")
        start_exam(name)

elif choice == "2":
    name = input("Enter your name: ")
    start_exam(name)

else:
    print("Invalid choice!")