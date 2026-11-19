
class ExpenseTracker:

    def __init__(self):
        self.transactions = []

    def add_income(self, amount, description):
        self.transactions.append({
            "type": "Income",
            "amount": amount,
            "description": description
        })
        print("Income added successfully!")

    def add_expense(self, amount, category):
        self.transactions.append({
            "type": "Expense",
            "amount": amount,
            "category": category
        })
        print("Expense added successfully!")

    def show_transactions(self):
        for item in self.transactions:
            print(item)

    def calculate_balance(self):
        income = sum(
            t["amount"] for t in self.transactions
            if t["type"] == "Income"
        )

        expense = sum(
            t["amount"] for t in self.transactions
            if t["type"] == "Expense"
        )

        print("Total Income:", income)
        print("Total Expense:", expense)
        print("Remaining Balance:", income - expense)

    def highest_expense_category(self):
        categories = {}

        for item in self.transactions:
            if item["type"] == "Expense":
                category = item["category"]
                categories[category] = (
                    categories.get(category, 0) + item["amount"]
                )

        if categories:
            print("Highest Expense:",
                  max(categories, key=categories.get))
        else:
            print("No expenses recorded.")


tracker = ExpenseTracker()

tracker.add_income(20000, "Salary")
tracker.add_expense(3000, "Food")
tracker.add_expense(2000, "Travel")
tracker.add_expense(4000, "Shopping")
tracker.add_expense(1500, "Food")

tracker.show_transactions()
tracker.calculate_balance()
tracker.highest_expense_category()
