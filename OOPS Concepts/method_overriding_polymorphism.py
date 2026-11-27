class Shape:
    def area(self) -> float:
        return 0.0

class Rectangle(Shape):
    def __init__(self, h: int, w: int):
        self.h = h
        self.w = w

    def area(self):
        return self.h * self.w

class Circle(Shape):
    def __init__(self, r: int):
        self.r = r

    def area(self):
        return 3.14 * self.r ** 2

shapes = [Rectangle(3, 4), Circle(3), Rectangle(4, 7)]
for s in shapes:
    print(s.area())