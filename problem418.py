def convert (s1):
    items= [s for s in s1.split('-')]
    items.sort()
    s2 = '-'.join(items)
    return s2
s = "here-comes-the=most-amazing-person"
t = convert(s)
print(t)