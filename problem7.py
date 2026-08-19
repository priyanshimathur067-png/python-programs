products = []
num = int(input("Enter the no. of products: "))
for i in range(num):
  value = input("Enter the products: ")
  products.append(value)
print("The list of products are :",products)
# items = input("Enter the items you want to delete : ")

# if items in products:
#   items.remove(value)
#   print("Items left in the cart: ",products)
# else:
#   print("Item not found ")

choice = input("Do you want to delete an item? (yes/no): ")

if choice == "yes":
    item = input("Enter the item you want to delete: ")

    if item in products:
        item.remove(value)
        print("Item deleted successfully!")
    else:
        print("Item not found!")

else:
    print("No item deleted.")

print("Final list:", products)
