class Student:
    def __init__(self, name: str) -> None:
        self.__name = name

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, new_name: str):
        if new_name != "":
            self.__name = new_name

s1 = Student("Mano")
print(s1.name)
s1.name = "Billi"
print(s1.name)