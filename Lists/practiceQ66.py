"""
using list comprehension, create a list of square of all odd numbers from 1 to 20.
"""
odd_num = [n*n for n in range(1, 21) if n %2 != 0]
print(odd_num)