# ask a name, age, gender
def greet(n, a, g):
    print(f"Hye! {n}, your age is {a} and your gender is {g}.")

name = input("Enter your name: ")
age = int(input("Enter your age: "))
gender = input("Enter your gender: ")
greet(name, age, gender)