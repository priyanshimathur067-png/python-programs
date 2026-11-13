
class Player:
    def __init__(self, name, score):
        self.name = name
        self.score = score

    def __lt__(self, other):
        return self.score < other.score


p1 = Player("Rahul", 85)
p2 = Player("Aman", 95)

if p1 < p2:
    print(p2.name, "has a higher score")
else:
    print(p1.name, "has a higher score")
