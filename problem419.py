def generate_list():
    lst = list()
    for i in range(1,11):
        lst.append((i,i**2,i**3))
        return lst
l = generate_list()
print(l)