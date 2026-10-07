"""
wrt a function called "square" that takes a number and returns its square.
store the result and print it.
"""
def square(n):
    return n*n
#or return n**2

n = int(input("Enter number = "))
result = square(n)
print(result)