"""
PAN Card Validation
Take a string as input. 
check if it is a valid pak PAN card  number.
format 5 uppercase + 4 digits + 1 uppercase letter.
"""
def pan_card_validation(text:str):
    char = list(text)
    # char_list = [*text]
    start = char[:5]
    start = "".join(start)
    mid = char[5:9]
    mid = "".join(mid)
    end = char[-1]
    if start.isupper() and mid.isdigit() and end.isupper():
        print("Valid")
    else:
        print("Invalid")

text = input("Enter a string: ")
pan_card_validation(text)