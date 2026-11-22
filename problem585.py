def atm_withdrawal(balance, withdraw):

    if withdraw <= 0:
        print("Invalid withdrawal amount")

    elif withdraw % 100 != 0:
        print("Amount must be a multiple of 100")

    elif withdraw > balance:
        print("Insufficient balance")

    else:
        balance = balance - withdraw

        print("Withdrawal Successful!")
        print("Withdrawn Amount:", withdraw)
        print("Remaining Balance:", balance)

balance = 10000
withdraw = 2500

atm_withdrawal(balance, withdraw)