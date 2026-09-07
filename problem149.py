def split_bill(bill, people, tip=0):

    tip_amount = bill * tip / 100

    total_bill = bill + tip_amount

    per_person = total_bill / people

    return total_bill, per_person


bill = 2400
people = 4

result = split_bill(bill, people, 10)

print("Total Bill:", result[0])
print("Each Person Pays:", result[1])