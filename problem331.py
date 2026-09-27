meters = [
    {"house": "A", "previous": 1250, "current": 1480},
    {"house": "B", "previous": 2100, "current": 2450},
    {"house": "C", "previous": 980, "current": 1100},
    {"house": "D", "previous": 3200, "current": 3900}
]

for meter in meters:
    units = meter["current"] - meter["previous"]
    meter["units"] = units

meters.sort(key=lambda x: x["units"], reverse=True)

for meter in meters:
    print(meter["house"], "→", meter["units"], "units")