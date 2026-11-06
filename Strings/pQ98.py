"""
Clean Phone Number
take a phone no as input in the format +92-32758-34834.
remove all dashes and the country code.
print the clean 10 digit number.
"""
def clean_phoneNo(phone_no:str):
    phone_no = phone_no.replace("-", "")
    phone_no = phone_no.replace("+92", "")
    print(phone_no)
phone_no = input("Enter your phone no(format +92-32758-34834): ")
clean_phoneNo(phone_no)
