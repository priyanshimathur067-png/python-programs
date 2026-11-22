def first_non_repeating(text):

    frequency = {}

    for ch in text:

        if ch in frequency:
            frequency[ch] += 1

        else:
            frequency[ch] = 1

    for i in range(len(text)):

        if frequency[text[i]] == 1:

            return text[i], i

    return -1

text = "aabbcddee"

result = first_non_repeating(text)

if result == -1:

    print("No non-repeating character found")

else:

    print("First Non-Repeating Character:", result[0])
    print("Index:", result[1])