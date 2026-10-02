def calculate_subscription(plan, months):
    plans = {
        "basic": 199,
        "standard": 399,
        "premium": 599
    }

    plan = plan.lower()

    if plan not in plans:
        return "Invalid plan"

    total = plans[plan] * months

    if months >= 12:
        discount = total * 0.10
        total = total - discount

    return total


plan = input("Enter plan (Basic/Standard/Premium): ")
months = int(input("Enter number of months: "))

result = calculate_subscription(plan, months)

if isinstance(result, str):
    print(result)
else:
    print("Total Subscription Cost: ₹", result)