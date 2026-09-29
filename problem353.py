videos = {
    "Python Tutorial": [5000, 600, 80],
    "DSA Basics": [7500, 700, 120],
    "Git Tutorial": [4500, 500, 100],
    "Django Tutorial": [9000, 800, 150]
}

engagements = {}

for video, data in videos.items():

    views = data[0]
    likes = data[1]
    comments = data[2]

    score = likes + (comments * 2)

    engagements[video] = score

    print(video)
    print("Views:", views)
    print("Engagement:", score)
    print()

highest_video = max(engagements, key=engagements.get)

average_views = sum(
    data[0] for data in videos.values()
) / len(videos)

print("Highest engagement:", highest_video)
print("Average views:", average_views)