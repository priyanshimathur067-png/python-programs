def search_product(products, target, index=0):
    if index == len(products):
        return False

    if products[index] == target:
        return True

    return search_product(products, target, index + 1)


products = ["Laptop", "Mouse", "Keyboard", "Mobile", "Tablet"]

target = "Mobile"

if search_product(products, target):
    print("Product found")
else:
    print("Product not found")