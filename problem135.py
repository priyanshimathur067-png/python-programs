def withdraw(balance, amount):
    if amount % 100 != 0:
        return "Amount must be a multiple of 100"

    if amount > balance:
        return "Insufficient balance"

    if balance - amount < 500:
        return "Minimum balance of ₹500 required"

    balance -= amount

    return f"Withdrawal successful\nRemaining balance: ₹{balance}"


balance = 10000
amount = 3000

print(withdraw(balance, amount))