# Job Applicant Analysis
registered = set(input("Enter registered people: ").split(","))
attended = set(input("Enter people who attended: ").split(","))

registered = {x.strip() for x in registered}
attended = {x.strip() for x in attended}

absent = registered - attended
unregistered = attended - registered

print("\nAbsent:", absent)
print("Attended without registration:", unregistered)
print("Total registered:", len(registered))
print("Total attended:", len(attended))