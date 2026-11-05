"""
checking content
isalpha(): all letters
isdigit(): all digits
isalnum(): either alpha or numeric or both(alphaNumeric)
isspace(): all whitespaces
startwith(): start with specific text
endwith(): end with specific text
"""
# text = "MahRukhUroojFatima"
# print(text.isalpha())
# text1 = "32537098"
# print(text.isdigit())
# print(text1.isdigit())
# text2 = "arifdu39r08"
# print(text.isalnum())
# print(text1.isalnum())
# print(text2.isalnum())
# text3 = "            \n \t    "
# print(text3.isspace())
# text4 = " "
# print(text4.isspace())
# text5 = "Mah Rukh"
# print(text5.startswith("Mah"))
# print(text5.endswith("Rukh"))


# practical example
age = input("Enter your age = ")
if age.isdigit():
    if int(age) >= 18: 
        print("You can vote")
    else: 
        print("You cannot vote")
else: 
    print("Please, enter valid age!")