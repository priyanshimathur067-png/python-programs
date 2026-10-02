def reserve_table(people, available_tables):
    if available_tables > 0:
        available_tables -= 1
        return available_tables
    else:
        return -1


people = int(input("Enter number of people: "))
tables = int(input("Enter available tables: "))

remaining_tables = reserve_table(people, tables)

if remaining_tables == -1:
    print("Sorry, no tables are available.")
else:
    print("Table reserved successfully.")
    print("Remaining tables:", remaining_tables)