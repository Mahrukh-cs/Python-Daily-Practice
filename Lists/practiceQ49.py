"""
create a list of 5 numbers. print first, middle and last element of list.
"""
nums = [10, 20, 30, 40, 50, 60, 70, 324]

n = len(nums)

print(f"First movie name = {nums[0]}")
print(f"Middle movie name = {nums[n//2]}")
# print(f"Last movie name = {nums[n-1]}")
print(f"Last movie name = {nums[-1]}")