expenses = {}

while True:
    category = input("Enter expense category: ")
    amount = float(input("Enter amount: "))

    if category in expenses:
        expenses[category] += amount
    else:
        expenses[category] = amount

    choice = input("Add another expense? (yes/no): ")

    if choice.lower() == "no":
        break

print("\nExpense Summary")

total = 0

for category, amount in expenses.items():
    print(category, ":", amount)
    total += amount

print("Total expenses:", total)

highest_category = max(expenses, key=expenses.get)

print("Highest spending category:", highest_category)
print("Amount spent:", expenses[highest_category])