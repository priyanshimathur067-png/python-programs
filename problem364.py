def login(username, password):
    correct_username = "admin"
    correct_password = "python123"

    if username == correct_username and password == correct_password:
        return True
    else:
        return False


attempts = 0

while attempts < 3:
    username = input("Enter username: ")
    password = input("Enter password: ")

    if login(username, password):
        print("Login successful!")
        break
    else:
        attempts += 1
        print("Invalid credentials.")

if attempts == 3:
    print("Account temporarily locked.")