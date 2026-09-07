def recharge(amount):

    plans = {
        199: "1.5 GB/day for 28 days",
        299: "2 GB/day for 28 days",
        399: "2.5 GB/day for 56 days",
        599: "3 GB/day for 84 days"
    }

    return plans.get(amount, "Plan not available")


amount = int(input("Enter recharge amount: "))

print(recharge(amount))