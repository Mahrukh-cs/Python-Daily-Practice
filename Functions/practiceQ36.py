"""
write a function that print all the factors of a number entered by user.
"""
def print_factors():
    n = int(input("Enter number = "))
    for i in range(1, n):
        if n%i == 0:
            print(i, end=" ")
    print(n)

print_factors()