"""
Email Validation
take an email as an input. 
validate that it contains exactly one @ and at least one . 
print valid or invalid.
"""
def check_email(email:str):
    if email.count("@") == 1 and "." in email:
        return "Valid"
    return "Invalid"


email = input("Enter your email: ")
print(check_email(email))
# if "@" and "." in email:
#     print("Valid")
# else: 
#     print("Invalid Email\nPlease, enter valid email")