class Animal:
    def breathe(self):
        print("Breathing...")

class Mammal(Animal):
    def eat(self):
        print("Eating...")

class Whale(Mammal):
    def sleep(self):
        print("Sleeping")


w = Whale()
w.breathe()     # from Animal class
w.eat()         # from Mammal class
w.sleep()       # from Whale class