def total_bill(prices, index=0):
    if index == len(prices):
        return 0

    return prices[index] + total_bill(prices, index + 1)


prices = [100, 250, 50, 300]

print("Total bill:", total_bill(prices))