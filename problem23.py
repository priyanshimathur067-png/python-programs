customer1 = set(input("Enter Customer 1 products: ").split(","))
customer2 = set(input("Enter Customer 2 products: ").split(","))
customer3 = set(input("Enter Customer 3 products: ").split(","))

customer1 = {x.strip() for x in customer1}
customer2 = {x.strip() for x in customer2}
customer3 = {x.strip() for x in customer3}

all_products = customer1 | customer2 | customer3

common = customer1 & customer2 & customer3

at_least_two = (
    (customer1 & customer2) |
    (customer2 & customer3) |
    (customer1 & customer3)
)

only_customer1 = customer1 - customer2 - customer3
only_customer2 = customer2 - customer1 - customer3
only_customer3 = customer3 - customer1 - customer2

only_one = only_customer1 | only_customer2 | only_customer3

print("\nProducts purchased by all:", common)
print("Products purchased by at least two:", at_least_two)
print("Products purchased by only one:", only_one)
print("Total unique products:", len(all_products))