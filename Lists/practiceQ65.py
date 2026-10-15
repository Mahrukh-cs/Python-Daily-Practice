"""
write a python script that iterates through a list of integers 
and replaces every negative number found in the list with the value 0.
"""
def replace_negative(ls):
    n = len(ls)
    for i in range(0, n):
        if ls[i] < 0:
            ls[i] = 0
    return ls

nums = [5, -3, 8, -1, 0, -10, 12]
print(f"Before nums = {nums}")
print(f"After nums = {replace_negative(nums)}")