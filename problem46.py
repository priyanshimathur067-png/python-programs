def bank_transactions(*transactions):
    balance = 0

    for amount in transactions:
        balance += amount

    print("Final Balance:", balance)


bank_transactions(5000, -1000, 2500, -500, 3000)