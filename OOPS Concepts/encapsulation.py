class BankAccount:
    def __init__(self, name: str, balance: int) -> None:
        self.name = name  
        self.__balance = balance

    def deposit(self, amount: int):
        if amount <= 0:
            print("Invalid Amount")
        else: 
            self.__balance += amount

    def get_balance(self):
        return self.__balance

acc = BankAccount("Mano", 100000000)
print(acc.name)
print(acc.get_balance())
acc.deposit(-11000)
acc.deposit(11000)
print(acc.get_balance())
# even after private attribute, still accessible. that is not real security
# print(acc._BankAccount__balance)