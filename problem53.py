def recharge_amount(plan, **details):
    plans = {
        "basic": 199,
        "standard": 399,
        "premium": 599
    }

    amount = plans.get(plan.lower(), 0)

    if amount == 0:
        return "Invalid plan"

    gst = amount * 0.18
    final_amount = amount + gst

    return final_amount


def show_recharge(plan, **details):
    result = recharge_amount(plan, **details)

    print("\n--- RECHARGE DETAILS ---")
    print("Plan:", plan)
    print("Final Amount: ₹", result)


show_recharge("standard", validity=56, data="2GB/day")