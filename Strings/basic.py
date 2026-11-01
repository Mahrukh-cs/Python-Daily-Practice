# string --> immutable
name = "mano"
print(name, id(name))
# TypeError: str object does not support item assignment
# name[0] = "b"
# print(name)

# override not update
name = "Billi"
print(name, id(name))



greeting = "Hello"
greeting = greeting + "World!"
print(greeting)