"""
given a list of numbers(which may contain duplicates),
write a python script that takes an integer as input from the user 
and removes all occurences of that integer from the list. 
"""
# my method
# def remove_occurence(nums,target):
#     n = len(nums)
#     for i in range(0, n):
#         if target in nums:
#             nums.remove(target)
#     return nums

# 2nd method
# def remove_occurence(nums,target):
#     new_list = []
#     for num in nums:
#         if num != target:
#             new_list.append(num)
#     return new_list

# 3rd method
def remove_occurence(ls,target):
    while target in ls:
        ls.remove(target)

nums = [10, 10, 10, 10, 20, 10, 30, 20, 10, 40]
target = int(input("Enter integer = "))
print(f"Before removing = {nums}")
# for print return list
# print(f"After removing = {remove_occurence(nums, target)}")

remove_occurence(nums, target)
print(f"After = {nums}")
