units = int(input("Enter electricity units consumed: "))

if units <= 100:
    print("Usage is low. No need to worry.")
elif units <= 250:
    print("Usage is moderate. Keep monitoring.")
elif units <= 400:
    print("High usage! Try reducing electricity consumption.")
else:
    print("Very high usage! Please check unnecessary appliances.")