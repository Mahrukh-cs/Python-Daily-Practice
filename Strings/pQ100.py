"""
Sorted Names
take a list names as input(comma seperated). split them, sort them alphabetically, 
and join them back with "|" as seperator.
"""
names = input("Enter a list names comma seperated: ")
nam = names.split(",")
print(nam)
nam.sort()
print(nam)
print(" | ".join(nam))