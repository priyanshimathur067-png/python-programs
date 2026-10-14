def first_unique(text):
    for ch in text:
        if text.count(ch) == 1:
            return ch
    return None

text = input("Enter a string: ")
result = first_unique(text)

if result is None:
    print("No unique character")
else:
    print("First non-repeating character:", result)
