class Animal:
    def __init__(self, name: str, age: int) -> None:
        self.name = name
        self.age = age

    def eat(self):
        print(f"{self.name} is eating.")

    def sleep(self):
        print(f"{self.name} is sleeping.")

class Cat(Animal):
    def speak(self):
        print(f"{self.name} is speaking meow, meow, meow.")

c = Cat("mano", 2)
c.eat()
c.sleep()
c.speak()