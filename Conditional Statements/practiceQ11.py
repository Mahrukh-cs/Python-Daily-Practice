"""
take a person's age and whether they have a valid ID (True/False) as input. 
they can enter a venue only if they are 18 or older and have a valid ID.
Print the appropriate message.
"""
age = int(input("Enter your age: "))
Id = input("Enter your ID (True or False): ")
if age >=18 and Id == "True":
    print("You're welcome.")
else:
    print("You can't enter venue.")

