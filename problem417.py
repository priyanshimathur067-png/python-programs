#Pangram is a sentencethat uses every letter of the alphabet.
def ispangram(s):
    alphaset = set("abcdefghijklmnopqrstuvwxyz")
    return alphaset <= set(s.lower())
print(ispangram("Hey I am good"))
print(ispangram('Crazy feedback'))