class Money:
    def __init__(self, amount):
        self.amount = amount

    def __eq__(self, other) -> bool:
        return self.amount == other.amount

    def __ls__(self, other) -> bool:
        return self.amount < other.amount

    def __le__(self, other):
        return self.amount <= other.amount

    def __gt__(self, other):
        return self.amount > other.amount

    def __ge__(self, other):
        return self.amount >= other.amount
    
a = Money(100)
b = Money(200)
print(a == b)
print(a < b)
print(a <= b)
print(a > b)
print(a >= b)