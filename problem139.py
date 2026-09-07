def track_order(status):

    messages = {
        "placed": "Your order has been placed.",
        "packed": "Your order has been packed.",
        "shipped": "Your order has been shipped.",
        "out_for_delivery": "Your order is out for delivery.",
        "delivered": "Your order has been delivered.",
        "cancelled": "Your order has been cancelled."
    }

    return messages.get(status, "Invalid order status")


status = input("Enter order status: ")

print(track_order(status))