"""
Logical Operators: used to combine multiple conditions together
and --> when both conditions are true
or --> when one condition is true
not --> opposite the condition
"""

physics = 75
chemistry = 35
print(physics > 33 and chemistry > 33)

chemistry = 31
print(physics > 33 or chemistry > 33)

print(not(True))
print(not(False))