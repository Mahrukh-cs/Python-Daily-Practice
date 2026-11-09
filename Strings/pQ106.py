"""
Word lengths
Take a sentence as input. Print each word's length next to it.
Example: Python(6) is(2) great(5).
"""
def word_length(text:str):
    words = text.split()
    for word in words:
        print(f"{word}({len(word)})", end=" ")

text = input("Enter a sentence: ")
words = text.split()
word_length(text)
