"""
numbers to cubes 
using dictionary comprehension, 
create a new dictionary where keys are numbers from 1 to 10(inclusive)
and values are cubes of each number.
"""
cubes = {}
cubes = {i: i * i * i for i in range(1, 11)}
print(cubes)