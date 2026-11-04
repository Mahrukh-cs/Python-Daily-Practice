"""
read a sentence from user. 
count and print total no of vowels(case-sensitive) present in it, using a for loop.
"""
sentence = input("Enter a sentence: ")
total = 0
for char in sentence:
    if char in "aeiouAEIOU":
        total += 1

print(f"Total vowels = {total}")