def shopping_cart(*prices):
    total = sum(prices)
    print("Items purchased:", len(prices))
    print("Total bill:", total)


shopping_cart(499, 299, 799, 150)