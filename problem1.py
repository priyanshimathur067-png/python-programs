f = open("poem.txt")
content = f.read()
if ("twinkle" in content):
    print ("The word is present")
else :
    print ("The word is not present")