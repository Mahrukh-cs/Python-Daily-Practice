"""
Capitalize long words
Take a sentence as input. Capitalize the first letter of each word contains less than 3 characters.
keep the rest as it.
"""
def capitalize_long_words(text:str):
    words = text.split()
    for word in words:
        if len(word) < 3:
            print(word.title(), end=" ")
        else:
            print(word, end=" ")

sent = input("Enter a sentence: ")
capitalize_long_words(sent)