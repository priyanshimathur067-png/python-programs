transactions = [5000, -1200, -500, 3000, -800, 1500]

deposits = []
withdrawals = []

for transaction in transactions:

    if transaction > 0:
        deposits.append(transaction)
    else:
        withdrawals.append(abs(transaction))

total_deposits = sum(deposits)
total_withdrawals = sum(withdrawals)

balance = total_deposits - total_withdrawals

print("Total deposits:", total_deposits)
print("Total withdrawals:", total_withdrawals)
print("Final balance:", balance)

print("Highest deposit:", max(deposits))
print("Highest withdrawal:", max(withdrawals))