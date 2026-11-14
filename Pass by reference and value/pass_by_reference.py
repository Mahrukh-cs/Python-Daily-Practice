# mutable objects are pass by reference
import copy
def add_num(x):
    x.append(99)
    # use copy if you don't want to make change outside
    # use deepcopy if nested 
    # x = copy.copy(x)
    # x.append(100)
    print(f"Inside function = {x}")

nums = [1, 2, 3]
add_num(nums)
print(f"Outside function = {nums}")