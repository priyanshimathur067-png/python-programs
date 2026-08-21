student1 = set(input("Enter Student 1 subjects: ").split(","))
student2 = set(input("Enter Student 2 subjects: ").split(","))

student1 = {x.strip() for x in student1}
student2 = {x.strip() for x in student2}

print("\nCommon subjects:", student1 & student2)
print("Only Student 1:", student1 - student2)
print("Only Student 2:", student2 - student1)
print("All subjects:", student1 | student2)