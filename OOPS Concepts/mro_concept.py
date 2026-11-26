# Diamond problem
class A:
    def hello(self):
        print("Hello from A")

class B(A):
    def hello(self):
        print("Hello from B")

class C(A):
    def hello(self):
        print("Hello from C")

class D(C, B):
    pass
    # def hello(self):
    #     print("Hello from D")

d = D()
d.hello()
print(D.__mro__)