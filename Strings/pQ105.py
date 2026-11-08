"""
Palindrome Check
wrt a function is_palindrome(text) that returns True if the given string is a palindrome
(ignore case and space)
"""
def is_palindrome(text:str):
    text = text.lower().replace(" ", "")
    return text == text[::-1]

text = input("Enter text: ")
print(is_palindrome(text))