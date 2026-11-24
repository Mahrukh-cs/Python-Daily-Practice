class Vehicle:
    def __init__(self, brand: str) -> None:
        self.brand = brand

    def start(self):
        print(f"{self.brand} starting up...")

class Car(Vehicle):
    def drive(self):
        print(f"{self.brand} is driving")

v = Vehicle("Corolla")
v.start()
# v.drive()         # AttributeError

c = Car("Toyota")
c.start()
c.drive()