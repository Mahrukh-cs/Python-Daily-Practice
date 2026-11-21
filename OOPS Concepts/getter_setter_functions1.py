class Student:
    def __init__(self, name: str) -> None:
        self.__name = name

    # setter
    def set_name(self, new_name: str) -> None:
        self.__name = new_name

    # getter
    def get_name(self):
        return self.__name

s1 = Student("Mano")
print(s1.get_name())
s1.set_name("Billi")
print(s1.get_name())