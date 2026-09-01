def word_counter(sentence):
    words = sentence.split()
    count = {}

    for word in words:
        count[word] = count.get(word, 0) + 1

    for word, frequency in count.items():
        print(word, ":", frequency)


sentence = "python is easy and python is powerful"

word_counter(sentence)