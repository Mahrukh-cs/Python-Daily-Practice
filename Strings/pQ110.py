"""
username verification
take a name input and print without extra spaces and only first letter of name should be captial.
"""
def print_name(name):
    name = name.strip().title()
    return name

name = input("Enter your name: ")
print(print_name(name))