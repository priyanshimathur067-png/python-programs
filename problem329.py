homes = {
    "Home A": 450,
    "Home B": 720,
    "Home C": 350,
    "Home D": 900,
    "Home E": 600
}

for home, usage in homes.items():
    if usage > 700:
        print(home, "→ High consumption")
    elif usage > 500:
        print(home, "→ Medium consumption")
    else:
        print(home, "→ Normal consumption")