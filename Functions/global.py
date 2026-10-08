# here name is global variable
name = "Mah Rukh"

def greet():
    # here name is local variable
    name = "Mano"
    print(f"Hey {name}! Good Morning")


greet()
print(name)
