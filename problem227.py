def characters(text):
    for char in text:
        yield char


for ch in characters("Python"):
    print(ch)