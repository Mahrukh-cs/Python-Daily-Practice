"""
write a function called "add" that takes 2 numbers as parameters and prints their sum.
"""
def add(n1, n2):
    sum = n1+n2
    print(f"Sum of {n1} and {n2} is {sum}")

n1 = int(input("Enter number 1 = "))
n2 = int(input("Enter number 2 = "))
add(n1, n2)