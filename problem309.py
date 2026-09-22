players = [
    ["Virat", 765],
    ["Rohit", 620],
    ["Gill", 845],
    ["Pant", 540],
    ["Jaiswal", 710]
]

players.sort(key=lambda x: x[1], reverse=True)

print("Cricket Batting Leaderboard")
print("---------------------------")

for i, player in enumerate(players):
    print("Rank", i + 1, "-", player[0], "-", player[1], "runs")