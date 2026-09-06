def total_payment(payment, months):
    if months == 0:
        return 0

    return payment + total_payment(payment, months - 1)


monthly_payment = 5000
months = 12

print("Total paid:", total_payment(monthly_payment, months))