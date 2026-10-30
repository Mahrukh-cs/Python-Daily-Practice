nums = {10, 40, 20, 50, 30}
print(len(nums))
print(min(nums))
print(max(nums))
print(sum(nums))
# sorted() --> gives you a new list containing all elements from the set in sorted order
#  but does'nt change original set
print(sorted(nums))
print(nums)
print(sorted(nums, reverse=True))

my_list = [1, 2, 3, 4, 5, 1]
print(my_list)
my_set = set(my_list)
print(my_set)
my_tuple = tuple(my_set)
print(my_tuple)