class student:
    def __init__(self, name: str, age: int, marks: list[int]):
        self.name = name
        self.age = age
        self.marks = marks

    def total(self) -> int:
        return sum(self.marks)

    def average(self) -> float:
        return sum(self.marks) / len(self.marks)

    def grade(self):
        avg = self.average()
        if avg >= 90:
            print("A")
        elif avg >= 75 and avg <= 89:
            print("B")
        else:
            print("C")
student1 = student("Mano", 20, [98, 99, 100])
total = student1.total()
print(total)
average = student1.average()
print(average)
student1.grade()