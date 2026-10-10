"""
create a list of 5 numbers {e.g: 10, 20, 30, 40, 50}. Replace the 2nd and 4th elements of this
list with the number 0 using indexing.
Print the updated list.
"""
nums = [10, 20, 30, 40, 50]

print(f"Before updating list = {nums}")

nums[1] = 0
nums[3] = 0

print(f"After updating list = {nums}")