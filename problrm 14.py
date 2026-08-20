def is_palindrome(text):
    return text == text[::-1]

text = input("Enter a word: ")

if is_palindrome(text):
    print("Palindrome")
else:
    print("Not a palindrome")