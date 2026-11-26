class Animal:
    def __init__(self, name: str) -> None:
        self.name = name

    def breathe(self):
        print(f"{self.name} is breathing")

class Cat(Animal):
    def meow(self):
        print("Meow!")

class Dog(Animal):
    def woof(self):
        print("Woof!")

class Cow(Animal):
    def moo(self):
        print("Mooo!")

c = Cat("Mano")
d = Dog("Rex")
cow = Cow("Bessie")

c.breathe()
d.breathe()
cow.breathe()