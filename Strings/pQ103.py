"""
username validation
take a username as input. strip any spaces from both sides 
and check if the cleaned name starts with a letter(not digit).
Print valid or invalid
"""
def validate_username(username:str):
    username = username.strip()
    if username[0].isalpha():
        return "Valid"
    return "Invalid"

username = input("Enter your name: ").strip()
print(validate_username(username))