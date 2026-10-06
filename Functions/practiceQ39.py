"""
write a function called find_max that takes three numbers as parameters 
and prints the largest one
"""
def find_max(n1, n2, n3):
    if n1 > n2 and n1 > n3:
        print(f"{n1} is largest number.")
    elif n2 > n1 and n2 > n3:
        print(f"{n2} is largest number.")
    else:
        print(f"{n3} is largest number.")

n1  = int(input("Enter number1 = "))
n2  = int(input("Enter number2 = "))
n3  = int(input("Enter number3 = "))
find_max(n1, n2, n3)