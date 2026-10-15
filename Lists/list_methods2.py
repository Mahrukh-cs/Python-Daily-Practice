"""
sorting, reversing, searching & counting
.sort() -->sort elements in ascending order directly, modify the original list
.sort(reverse=True) --> sort elements in descending order, modify the original list
.reverse()  --> reverse the order of list(not in descending), modify the original list
.index()    --> returns the index of first occurence of a specified value in the list
.count()    --> returns the number of value appears in the list
"""
nums = [2, 1, 7, 4, 9, -3, 0, 42]
# sorted() --> will return a new list
# new_list = sorted(nums)
# print(f"New list = {new_list} and id =  {id(new_list)}")
# print(f"Old list = {nums} and id =  {id(nums)}")


# sort() will change in that list. (In-place sorting)
nums.sort()
# nums.sort(reverse=True)    # descending order
print(f"nums = {nums} and id =  {id(nums)}")
print(f"nums = {nums} and id =  {id(nums)}")