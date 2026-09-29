tables = {
    1: "Available",
    2: "Occupied",
    3: "Available",
    4: "Available",
    5: "Occupied",
    6: "Available"
}

table_number = int(input("Enter table number: "))

if tables.get(table_number) == "Available":

    tables[table_number] = "Occupied"
    print("Table reserved successfully.")

else:
    print("Table is not available.")

print("\nAvailable tables:")

for table, status in tables.items():
    if status == "Available":
        print("Table", table)