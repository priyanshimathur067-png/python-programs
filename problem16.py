def calculate_bill(prices):
    total = 0

    for price in prices:
        total += price

    return total

prices = []

n = int(input("How many products? "))

for i in range(n):
    price = float(input("Enter product price: "))
    prices.append(price)

total = calculate_bill(prices)

print("Total Bill:", total)