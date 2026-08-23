sentence = input("Enter a sentence: ")
word = input("Enter word to search: ")

if word.lower() in sentence.lower():
    print("Word found")
else:
    print("Word not found")