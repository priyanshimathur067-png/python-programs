def long_words(words):
    for word in words:
        if len(word) > 4:
            yield word


words = ["cat", "apple", "banana", "dog", "python"]

for word in long_words(words):
    print(word)