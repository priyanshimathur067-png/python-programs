
def longest_word(sentence):
    words = sentence.split()
    longest = ""

    for word in words:
        if len(word.strip(".,!?")) > len(longest.strip(".,!?")):
            longest = word

    return longest.strip(".,!?")


sentence = input("Enter a sentence: ")
print("Longest word:", longest_word(sentence))
