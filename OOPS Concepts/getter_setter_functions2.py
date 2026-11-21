class Person:
    def __init__(self, age):
        self.__age = age

    def set_age(self, age: int):
        if age < 0:
            raise ValueError("Age must be non-negative")
        elif age == 0:
            raise ValueError("Age cannot be zero")
        self.__age = age

    def get_age(self):
        return self.__age

p1 = Person(21)
print(p1.get_age())
p1.set_age(22)
print(p1.get_age())