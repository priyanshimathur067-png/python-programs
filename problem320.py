transactions = [
    ("Deposit", 5000),
    ("Withdraw", 1500),
    ("Deposit", 3000),
    ("Withdraw", 500),
    ("Deposit", 2000)
]

total_deposit = 0
total_withdraw = 0

for transaction, amount in transactions:

    if transaction == "Deposit":
        total_deposit += amount

    elif transaction == "Withdraw":
        total_withdraw += amount

print("Total Deposits:", total_deposit)
print("Total Withdrawals:", total_withdraw)

balance = total_deposit - total_withdraw

print("Final Balance:", balance)

largest = max(transactions, key=lambda x: x[1])

print("Largest Transaction:", largest)