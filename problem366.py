def analyze_resume(resume, required_skills):
    resume = resume.lower()

    matched = []
    missing = []

    for skill in required_skills:
        if skill.lower() in resume:
            matched.append(skill)
        else:
            missing.append(skill)

    percentage = (len(matched) / len(required_skills)) * 100

    return matched, missing, percentage


required_skills = ["Python", "SQL", "Django", "Git"]

resume = input("Enter your resume summary: ")

matched, missing, percentage = analyze_resume(resume, required_skills)

print("\nMatched Skills:", matched)
print("Missing Skills:", missing)
print("Match Percentage:", round(percentage, 2), "%")