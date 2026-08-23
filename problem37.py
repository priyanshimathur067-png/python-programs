products = "laptop, mobile, keyboard, mouse, headphones"

search = input("Enter product name: ").lower()

if search in products:
    print("Product is available")
else:
    print("Product is not available")