def login(**credentials):
    username = credentials.get("username")
    password = credentials.get("password")

    if username == "admin" and password == "1234":
        print("Login successful")
    else:
        print("Invalid username or password")


login(username="admin", password="1234")