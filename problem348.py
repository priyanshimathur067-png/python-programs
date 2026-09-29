posts = {
    "Post 1": [500, 40, 20],
    "Post 2": [800, 50, 35],
    "Post 3": [650, 80, 40],
    "Post 4": [900, 30, 25],
    "Post 5": [700, 70, 50]
}

engagements = {}

for post, data in posts.items():

    likes = data[0]
    comments = data[1]
    shares = data[2]

    score = likes + (comments * 2) + (shares * 3)

    engagements[post] = score

    print(post, "Engagement:", score)

average = sum(engagements.values()) / len(engagements)

highest_post = max(engagements, key=engagements.get)

print("\nAverage engagement:", average)
print("Highest engagement:", highest_post)