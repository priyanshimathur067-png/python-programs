def employee_profile(**details):
    print("Employee Profile")

    for key, value in details.items():
        print(key.title(), ":", value)


employee_profile(
    name="Priyanshi",
    role="Software Developer",
    experience="Fresher",
    skills="Python, Java, SQL"
)