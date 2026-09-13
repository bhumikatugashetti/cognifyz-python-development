def is_palindrome(text):
    text = text.lower()
    return text == text[::-1]


text = input("Enter a word: ")

if is_palindrome(text):
    print("It is a palindrome.")
else:
    print("It is not a palindrome.")
    