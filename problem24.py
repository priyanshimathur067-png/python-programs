# Three days Attendance
monday = set(input("Enter Monday students: ").split(","))
tuesday = set(input("Enter Tuesday students: ").split(","))
wednesday = set(input("Enter Wednesday students: ").split(","))

monday = {x.strip() for x in monday}
tuesday = {x.strip() for x in tuesday}
wednesday = {x.strip() for x in wednesday}

all_students = monday | tuesday | wednesday

all_three = monday & tuesday & wednesday

mon_tue_not_wed = (monday & tuesday) - wednesday

only_monday = monday - tuesday - wednesday

print("\nPresent all three days:", all_three)
print("Monday + Tuesday but not Wednesday:", mon_tue_not_wed)
print("Only Monday:", only_monday)
print("Total students who attended:", len(all_students))