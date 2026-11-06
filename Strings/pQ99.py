"""
Vowel Starting words
Take a sentence as input. 
split it into words and print how many words start with a vowel. 
"""
def count_vowel_words(sentence:str):
    vowels = "aeiouAEIOU"
    count = 0
    words = sentence.split()
    for word in words:
        if word[0] in vowels:
            count +=1
    return count
# sentence = "Mahrukh is excellent software engineer"
sentence = input("Enter a sentence : ")
print(count_vowel_words(sentence))
# sen = sentence.split()
# count = 0
# for word in sen:
#     if word.startswith(('a', 'e', 'i', 'o', 'u')):
#         count +=1
# print(count)