text = "Programming and Logic"
# vowels = 0
# for char in text:
#     if (
#           char == "a" 
#        or char == "e" 
#        or char == "i" 
#        or char == "o" 
#        or char == "u" 
#        or char == "A" 
#        or char == "E" 
#        or char == "I" 
#        or char == "O" 
#        or char == "U"
#     ):
#         vowels += 1
# print(vowels)

vowels = 0
for char in text:
    if char in "aeiouAEIOU":
        vowels += 1

print(vowels)