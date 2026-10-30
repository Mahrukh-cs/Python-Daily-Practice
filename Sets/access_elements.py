fruits = {"apple", "banana", "kiwi"}
print("banana" in fruits)


# practical use
allowed_users = {"mano", "billi", "rukh"}
user = input("Enter your name: ")
if user in allowed_users:
    print("Access granted")
else: 
    print("Access denied")