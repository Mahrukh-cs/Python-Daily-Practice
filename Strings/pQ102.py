"""
Longest word
take a sentence as input. print the longest word in
"""
def print_longest_word(sentence:str):
    words = sentence.split()
    print(max(words, key= lambda x: len(x)))
    # longest_count = 0
    # longest_word = ""
    # for word in words:
    #     if len(word) > longest_count:
    #         longest_count = len(word)
    #         longest_word = word
    # print(longest_word)
sent = input("Enter a sentence: ")
print_longest_word(sent)