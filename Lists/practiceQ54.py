"""
take a list as input and a target number. use loop to determine if target exists in list. 
Don't use in operator.
"""

def does_target_exists(lst, target):
    for num in lst:
        if num == target:
            return True
    return False

nums = [6, -4, 20, -3, 32, 50, -4, 3, -6]
target = int(input("Enter target number = "))
print(does_target_exists(nums, target))

