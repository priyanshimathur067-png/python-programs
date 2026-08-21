# EMPLOYEE SKILL MATCHUING
employee_skill = set(input("Enter employee skills: ").split(","))
required_skill = set(input("Enter required skills : ").split(","))
employee_skill = {skill.strip() for skill in employee_skill}
required_skill = {skill.strip() for skill in required_skill}
available_skill = employee_skill & required_skill
missing_skill = required_skill - employee_skill
print("skills employee has:",available_skill)
print("Missing Skill: ",missing_skill)
if not missing_skill:
    print("Status : Employee is fully qualified")
else:
    print("Status : Employee is not fully qualified")