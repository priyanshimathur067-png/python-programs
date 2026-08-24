def apply_for_job(name, *skills, **details):
    print("Applicant:", name)

    print("\nSkills:")
    for skill in skills:
        print("-", skill)

    print("\nApplication Details:")
    for key, value in details.items():
        print(key.title(), ":", value)


apply_for_job(
    "Priyanshi",
    "Python",
    "Java",
    "SQL",
    "HTML",
    "CSS",
    role="Software Developer",
    experience="Fresher",
    location="India"
)