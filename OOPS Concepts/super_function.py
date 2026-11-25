class Animal:
    def __init__(self, name: str) -> None:
        self.name = name

    def speak(self):
        print(f"Animal is speaking")

    def eat(self):
        print(f"Animal is eating")

class Cat(Animal):
    def speak(self):
        # super()
        super().speak()
        print(f"Cat is speaking")

    def sleep(self):
        print(f"Cat is sleeping")

    def eat(self):
        print(f"Cat is eating food")


c = Cat("Mano")
# method overriding
c.speak()
c.eat()
c.sleep()