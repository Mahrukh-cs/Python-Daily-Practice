"""
given two lists, merge them into a single new list without modifying the originals 
hint: use + operator or loop to combine 
"""
def merge_two_lists(ls1, ls2):
    return ls1+ls2


num1 = [1, 2, 3, 4, 5]
num2 = [6, 7, 8, 9, 10]
# other way 
# num3 = []
# num3 = num1 + num2

print(merge_two_lists(num1, num2))
