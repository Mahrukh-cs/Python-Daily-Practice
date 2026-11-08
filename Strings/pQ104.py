"""
Unique words count
Take a paragraph as input. Print the count of unique words in it(case insensitive).
"""
def count_unique_words(para:str):
    words = para.split()
    return len(set(words))

paragraph = input("Enter a paragraph: ")
print(count_unique_words(paragraph))