def unique_emails(emails):
    unique = set(emails)

    print("Unique Emails:")

    for email in unique:
        print(email)


emails = [
    "a@gmail.com",
    "b@gmail.com",
    "a@gmail.com",
    "c@gmail.com",
    "b@gmail.com"
]

unique_emails(emails)