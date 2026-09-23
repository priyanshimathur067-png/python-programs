bill = float(input("Enter total bill: "))
people = int(input("Enter number of people: "))
tip_percentage = float(input("Enter tip percentage: "))

tip = bill * tip_percentage / 100
total_bill = bill + tip

amount_per_person = total_bill / people

print("Food bill:", bill)
print("Tip:", tip)
print("Total bill:", total_bill)
print("Each person pays:", amount_per_person)