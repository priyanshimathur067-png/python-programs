applicants = [
    ["Priya", 85, 90],
    ["Aman", 92, 78],
    ["Riya", 88, 95],
    ["Rahul", 75, 82]
]

# Calculate total score
for applicant in applicants:
    applicant.append(applicant[1] + applicant[2])

# Sort by total score in descending order
applicants.sort(key=lambda x: x[3], reverse=True)

print("Job Applicant Ranking")
print("---------------------")

rank = 1

for applicant in applicants:
    print(
        rank,
        applicant[0],
        "Aptitude:", applicant[1],
        "Technical:", applicant[2],
        "Total:", applicant[3]
    )
    rank += 1