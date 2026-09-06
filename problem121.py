def total_bill(prices, n):
    if n == 0:
        return 0
    return prices[n - 1] + total_bill(prices, n - 1)

prices = [200, 450, 150, 300]
print("Total bill:", total_bill(prices, len(prices)))


# Total bill recovery
