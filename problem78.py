def grocery_bill(prices):
    print("Total Amount:", sum(prices))
    print("Highest Price:", max(prices))
    print("Lowest Price:", min(prices))
    print("Number of Items:", len(prices))


prices = [120, 250, 80, 300, 150]

grocery_bill(prices)