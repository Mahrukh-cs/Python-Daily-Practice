"""
take a name as input from user. 
print its first character, its last character and total length of name.
"""
name = input("Enter your name: ")
print(f"First char = {name[0]}")
print(f"Last char = {name[-1]}")
print(f"Length = {len(name)}")