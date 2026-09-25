"""
Operator Precedence : when multiple operators are in one expression, python follows a sepcific order just like BODMAS rule in maths
Order: 
() 
**
*, /, //, %
+ , -
"""
print(2+3*4)
print(10-2**3)
print(10//2+3)

# use parenthesis to force the operation you want
print((2+3)*4)
print((10-2)**3)
