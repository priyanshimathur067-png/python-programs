tables = {
    1: "Available",
    2: "Booked",
    3: "Available",
    4: "Available",
    5: "Booked"
}

table_no = int(input("Enter table number: "))

if table_no in tables:
    if tables[table_no] == "Available":
        tables[table_no] = "Booked"
        print("Table booked successfully!")
    else:
        print("Sorry, table is already booked.")
else:
    print("Invalid table number.")

print(tables)