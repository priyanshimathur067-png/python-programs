def analyze_transactions(transactions):

    deposits = 0
    withdrawals = 0

    for transaction in transactions:

        if transaction > 0:
            deposits += transaction
        else:
            withdrawals += abs(transaction)

    balance = deposits - withdrawals

    return deposits, withdrawals, balance


transactions = [5000, -1000, -500, 2000, -300]

result = analyze_transactions(transactions)

print("Total Deposits:", result[0])
print("Total Withdrawals:", result[1])
print("Final Balance:", result[2])