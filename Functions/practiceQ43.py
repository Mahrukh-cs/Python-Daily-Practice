"""
wrt a function called ""absolute_value that takes a number 
and returns its absolute value without using the built-in abs() function.
"""
def absolut_value(n):
    if n >= 0:
        return n
    return n*-1

n = int(input("Enter number = "))
print(absolut_value(n))
