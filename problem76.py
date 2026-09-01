def permission(func):
    def wrapper():
        role = "admin"

        if role == "admin":
            func()
        else:
            print("Access Denied")

    return wrapper


@permission
def delete_record():
    print("Record deleted")


delete_record()