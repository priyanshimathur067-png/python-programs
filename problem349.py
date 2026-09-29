medicines = {
    "Paracetamol": 2025,
    "Vitamin C": 2026,
    "Cough Syrup": 2027,
    "Antibiotic": 2025,
    "Pain Relief": 2026
}

current_year = int(input("Enter current year: "))

expired = []
expiring_this_year = []
safe = []

for medicine, expiry_year in medicines.items():

    if expiry_year < current_year:
        expired.append(medicine)

    elif expiry_year == current_year:
        expiring_this_year.append(medicine)

    else:
        safe.append(medicine)

print("Expired medicines:", expired)
print("Expiring this year:", expiring_this_year)
print("Safe medicines:", safe)