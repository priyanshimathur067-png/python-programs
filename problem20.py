# Library Book Return 
issued = set(input("Enter issued books: ").split(","))
returned = set(input("Enter returned books: ").split(","))

issued = {x.strip() for x in issued}
returned = {x.strip() for x in returned}

not_returned = issued - returned
extra_returned = returned - issued

print("\nBooks not returned:", not_returned)
print("Invalid/extra returned books:", extra_returned)
print("Total books issued:", len(issued))