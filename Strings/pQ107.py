"""
Reverse Word Order
Take a sentence as input. Reverse the order of words(not the characters in each word)
e.g: Python is fun  --> fun is python
"""
def reverse_word_order(text:str):
    words = text.split()
    words = words[::-1]
    return " ".join(words)

sent = input("Enter a sentence: ")
print(reverse_word_order(sent))